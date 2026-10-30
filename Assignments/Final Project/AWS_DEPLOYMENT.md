# Deploying the Survey App on AWS (EC2 + MongoDB Atlas)

This guide hosts the Flask app on an **Amazon EC2** Ubuntu server, using **Gunicorn** (runs the Python app) behind **Nginx** (the public web server), and stores data in **MongoDB Atlas** (MongoDB's free cloud database).

```
Browser ──HTTP:80──▶ Nginx ──▶ Gunicorn :8000 ──▶ Flask app (app.py) ──▶ MongoDB Atlas
                    └────────────── EC2 instance (Ubuntu) ──────────────┘
```

Budget about 45–60 minutes the first time.

**You'll need:**
- An AWS account: <https://aws.amazon.com/free>
- A MongoDB Atlas account: <https://www.mongodb.com/cloud/atlas/register>
- A GitHub account with this project pushed to a repository (Step 2)

> **Cost:** a `t2.micro` / `t3.micro` instance is free-tier eligible, and the Atlas M0 cluster is free. AWS charges a small hourly fee for public IPv4 addresses, and free-tier terms vary by account, so check **Billing → Free Tier** in the AWS console. Step 11 shows how to shut everything down after grading.

---

## Step 1: Create the MongoDB Atlas database

1. Log in to Atlas and click **Create** to make a new cluster. Choose the **M0 (Free)** tier, provider **AWS**, region **N. Virginia (us-east-1)**, then click **Create Deployment**.
2. **Create a database user.** Atlas prompts you to do this when the cluster is created. You can also go to **Security → Database Access → Add New Database User**.
   - Authentication: **Password**
   - Username, for example `survey_app`
   - Password: click **Autogenerate Secure Password** and save it somewhere safe. A password with only letters and numbers avoids URL-encoding problems.
   - Role: **Read and write to any database**
3. **Allow network access.** Go to **Security → Network Access → Add IP Address**.
   - For now, click **Add Current IP Address** so you can test from your own computer.
   - You'll add the EC2 server's IP in Step 5.
4. **Get the connection string.** Go to **Database → Connect → Drivers → Python** and copy the string. It looks like this:
   ```
   mongodb+srv://survey_app:<db_password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   ```
   Replace `<db_password>` with the real password.
5. **Test it locally.** In the project folder on your computer, copy `.env.example` to `.env` and set `MONGO_URI` to the connection string. Then run:
   ```bash
   python seed_data.py 200     # inserts 200 sample responses
   ```
   In Atlas, open **Browse Collections**. You should see the `healthcare_survey` database with a `users` collection.

## Step 2: Push the project to GitHub

1. On GitHub, create a new repository, for example `healthcare-survey`. Public is easiest, because the server can then clone it without a login.
2. In the project folder, run:
   ```bash
   git init
   git add .
   git commit -m "Healthcare spending survey app"
   git branch -M main
   git remote add origin https://github.com/<your-username>/healthcare-survey.git
   git push -u origin main
   ```
   `.env` is listed in `.gitignore`, so your database password is **not** uploaded. Double-check that it doesn't appear on GitHub.

## Step 3: Launch an EC2 instance

1. Log in to the AWS Console. Pick a region in the top-right corner, for example **US East (N. Virginia)**, and open **EC2 → Instances → Launch instances**.
2. Fill in the form:
   - **Name:** `healthcare-survey`
   - **AMI:** **Ubuntu Server 24.04 LTS** (marked "Free tier eligible")
   - **Instance type:** `t2.micro` or `t3.micro` (whichever is marked free-tier eligible)
   - **Key pair:** click **Create new key pair**. Name it `healthcare-key`, type **RSA**, format **.pem**. The file downloads; keep it safe, because you can't download it again.
   - **Network settings:**
     - ☑ **Allow SSH traffic from: My IP**
     - ☑ **Allow HTTP traffic from the internet**
   - **Storage:** the default 8 GiB is fine
3. Click **Launch instance**, then **View all instances**. Wait until **Instance state = Running** and **Status checks = 2/2 passed**.

## Step 4: Give the server a fixed IP (Elastic IP)

Without this step, the public IP changes every time the instance is stopped and started.

1. Go to **EC2 → Network & Security → Elastic IPs → Allocate Elastic IP address → Allocate**.
2. Select the new address, then **Actions → Associate Elastic IP address**. Choose your `healthcare-survey` instance and click **Associate**.
3. Write down this IP. It's your app's address, for example `54.123.45.67`.

## Step 5: Let the server reach Atlas

In Atlas, go to **Security → Network Access → Add IP Address**. Enter the Elastic IP from Step 4 (for example `54.123.45.67/32`) and click **Confirm**.

## Step 6: Connect to the server

**Option A, browser (simplest):** in EC2, select the instance and click **Connect → EC2 Instance Connect → Connect**. A terminal opens in your browser.

**Option B, SSH from Windows PowerShell:**
```powershell
# One time only: restrict the key file's permissions, or SSH refuses to use it
icacls "C:\path\to\healthcare-key.pem" /inheritance:r /grant:r "$($env:USERNAME):R"

ssh -i "C:\path\to\healthcare-key.pem" ubuntu@54.123.45.67
```
Type `yes` when asked to trust the host.

All the commands from here to Step 9 run **on the server**.

## Step 7: Install the app on the server

```bash
# System packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip nginx git

# Get the code (the folder name must be healthcare-survey: the service file expects it)
cd ~
git clone https://github.com/<your-username>/healthcare-survey.git healthcare-survey
cd healthcare-survey

# Python virtual environment + app dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create the server's `.env` file:
```bash
cp .env.example .env
nano .env
```
- Set `MONGO_URI` to your Atlas connection string.
- Set `FLASK_SECRET_KEY` to a random value. You can generate one with `python3 -c "import secrets; print(secrets.token_hex(32))"`.
- In nano, save with **Ctrl+O**, **Enter**, and exit with **Ctrl+X**.

Quick test:
```bash
gunicorn --bind 127.0.0.1:8000 app:app &
sleep 2
curl http://127.0.0.1:8000/health        # should print {"status":"ok"}
kill %1
```

## Step 8: Run the app as a service (systemd)

A service keeps the app running after you log out, and restarts it if it crashes or the server reboots.

```bash
sudo cp deploy/healthcare-survey.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now healthcare-survey
sudo systemctl status healthcare-survey     # look for "active (running)"; press q to exit
```

## Step 9: Put Nginx in front

```bash
sudo cp deploy/nginx-healthcare-survey.conf /etc/nginx/sites-available/healthcare-survey
sudo ln -s /etc/nginx/sites-available/healthcare-survey /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t                  # should say "syntax is ok" and "test is successful"
sudo systemctl restart nginx
```

## Step 10: Test it

1. In your browser, open **http://54.123.45.67** (your Elastic IP; note **http**, not https).
2. Submit a response. You should land on the "Thank you!" page.
3. In Atlas **Browse Collections**, the new document appears in `healthcare_survey.users`.
4. For your submission, take screenshots of the live form, the thank-you page, the Atlas collection, and the EC2 instance running. Put the URL in the README.

**Updating the app later:**
```bash
cd ~/healthcare-survey && git pull
source venv/bin/activate && pip install -r requirements.txt
sudo systemctl restart healthcare-survey
```

## Step 11: Shut down after grading (to avoid charges)

1. EC2 → Instances → select the instance → **Instance state → Terminate**.
2. EC2 → Elastic IPs → select the IP → **Actions → Release Elastic IP address**. An unattached Elastic IP still costs money.
3. Optionally, delete the Atlas cluster.

---

## Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| Browser times out / "can't reach site" | The security group doesn't allow HTTP. Go to EC2 → instance → **Security** tab → security group → **Edit inbound rules** and add **HTTP, port 80, source 0.0.0.0/0**. Also make sure you used `http://`, not `https://`. |
| **502 Bad Gateway** | Gunicorn isn't running. Check `sudo systemctl status healthcare-survey` and `sudo journalctl -u healthcare-survey -n 50`. |
| Form submit hangs, then errors with `ServerSelectionTimeoutError` | Atlas is blocking the server. Add the Elastic IP under Atlas **Network Access** (Step 5). |
| `bad auth : authentication failed` | Wrong username/password in `MONGO_URI`. If the password has special characters (`@ : / ? # %`), URL-encode them or create a new password with letters and numbers only. After editing `.env`, run `sudo systemctl restart healthcare-survey`. |
| SSH: `UNPROTECTED PRIVATE KEY FILE` | Run the `icacls` command from Step 6. |
| SSH: connection timed out | Your home IP changed. Edit the security group's SSH rule to **My IP** again, or use EC2 Instance Connect. |
| `status=203/EXEC` in the service logs | The project isn't at `/home/ubuntu/healthcare-survey`, or the venv is missing. Re-check Step 7. |
