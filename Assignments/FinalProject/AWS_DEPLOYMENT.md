# Deploying the Survey App on AWS

These are the steps I followed to get the app running at <http://16.192.107.188/>. The Flask app runs on an Ubuntu server on **Amazon EC2**: **Gunicorn** runs the Python code, **Nginx** handles the web traffic, and the responses are saved in **MongoDB Atlas**, MongoDB's free cloud database.

```
Browser ──HTTP:80──▶ Nginx ──▶ Gunicorn :8000 ──▶ Flask app (app.py) ──▶ MongoDB Atlas
                    └────────────── EC2 instance (Ubuntu) ──────────────┘
```

It took me around an hour the first time, mostly because of the issues listed in [Things that tripped me up](#things-that-tripped-me-up).

**What you need first:**
- An AWS account (<https://aws.amazon.com/free>). It has to be a full AWS account. An "AWS Builder ID" won't let you launch servers.
- A MongoDB Atlas account (<https://www.mongodb.com/cloud/atlas/register>)
- The project pushed to GitHub (Step 2)

> **Cost:** a `t3.micro` server and the Atlas M0 cluster are both free-tier eligible. AWS does charge a small amount for public IPv4 addresses, including Elastic IPs (about $3.60 a month each). Step 11 covers shutting everything down afterwards.

---

## Step 1: Set up the MongoDB Atlas database

1. In Atlas, click **Create** and choose the **M0 (Free)** cluster on **AWS**. Pick a region close to where your server will be.
2. **Create a database user** (Atlas asks for this straight away, or go to **Security → Database Access**).
   - Authentication: **Password**
   - Username: something like `survey_app`
   - Password: letters and numbers only. Symbols like `@` or `:` break the connection string unless you encode them.
   - Role: **Read and write to any database**
3. **Network access:** go to **Security → Network Access → Add IP Address → Add Current IP Address** so your own computer can connect. The server's IP gets added in Step 5.
4. **Connection string:** **Connect → Drivers → Python**. It looks like this:
   ```
   mongodb+srv://survey_app:<db_password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   ```
   Put your real password in place of `<db_password>`.
5. **Test it from your computer:** copy `.env.example` to `.env`, paste the connection string into `MONGO_URI`, then run `python seed_data.py 200`. In Atlas, **Browse Collections** (now called **Data Explorer**) should show a `healthcare_survey` database with a `users` collection.

You don't need to create or name the database yourself. MongoDB creates it the first time something is saved.

## Step 2: Push the project to GitHub

I keep all my coursework in one public repository, [`nxu`](https://github.com/abdallahdataguy/nxu), so this project lives in its [`Assignments/FinalProject`](https://github.com/abdallahdataguy/nxu/tree/main/Assignments/FinalProject) folder. Because the repo is public, the server can clone it without logging in. To add the project, copy its files into that folder of your local clone, then:

```bash
cd nxu
git add Assignments/FinalProject
git commit -m "Add final project: healthcare spending survey"
git push
```

Before committing, run `git status` and check that `venv/` and `.env` are **not** in the list. Both are in `.gitignore`, so your database password stays on your computer.

## Step 3: Launch the EC2 server

1. Sign in to the AWS Console and choose a region in the top-right corner. I used **Europe (Stockholm), eu-north-1**. Search for **EC2** and click **Launch instance**.
2. Fill in the form:
   - **Name:** `healthcare-survey`
   - **AMI:** Ubuntu Server 24.04 LTS (free tier eligible)
   - **Instance type:** `t3.micro`
   - **Key pair:** **Create new key pair** → name `healthcare-key`, type RSA, format `.pem`. Keep the file safe; AWS only lets you download it once.
   - **Network settings:**
     - ☑ Allow SSH traffic from **My IP** (only your computer can try to log in)
     - ☑ Allow HTTP traffic from the internet (so anyone can open the website)
   - **Storage:** the default 8 GiB is plenty
3. Click **Launch instance** and wait until the instance shows **Running** with all status checks passed.

## Step 4: Give the server a fixed address (Elastic IP)

A new server's public IP changes every time it stops and starts, so it needs a fixed one.

1. **EC2 → Elastic IPs → Allocate Elastic IP address → Allocate.** Click it only once. I ended up with five by accident, and each one costs money whether it's used or not.
2. Select the address → **Actions → Associate Elastic IP address** → choose the `healthcare-survey` instance → **Associate**.
3. The instance's **Public IPv4 address** now shows the Elastic IP. Mine is `16.192.107.188`. The original address is gone, and it can't be turned into an Elastic IP.

## Step 5: Let the server talk to Atlas

In Atlas, **Security → Network Access → Add IP Address** → enter the Elastic IP with `/32` on the end (`16.192.107.188/32`) → **Confirm**.

Keep your own computer's IP on the list too if you want to run `export_to_csv.py` locally.

## Step 6: Connect to the server

**Option A: in the browser.** Select the instance → **Connect → EC2 Instance Connect → Connect**.

This failed for me at first with *"Error establishing SSH connection"*. The browser connection actually comes from AWS's own servers, not from my computer, so the **My IP** rule blocks it. The fix is a second inbound SSH rule in the security group, with its source set to **com.amazonaws.eu-north-1.ec2-instance-connect**. Type `ec2-instance-connect` in the source box to find it, and pick your own region's entry if you're not in Stockholm.

**Option B: from PowerShell on Windows.**
```powershell
# one time only: lock down the key file, or SSH refuses to use it
icacls "C:\path\to\healthcare-key.pem" /inheritance:r /grant:r "$($env:USERNAME):R"

ssh -i "C:\path\to\healthcare-key.pem" ubuntu@16.192.107.188
```

Everything from here to Step 9 runs **on the server**.

## Step 7: Install the app

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip nginx git

cd ~
git clone https://github.com/abdallahdataguy/nxu.git
ln -s ~/nxu/Assignments/FinalProject ~/healthcare-survey
cd ~/healthcare-survey

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The `ln -s` line creates a shortcut, `~/healthcare-survey`, that points to the project folder inside the repo. The service file in Step 8 expects the app at `/home/ubuntu/healthcare-survey`, so the shortcut means it doesn't need changing.

Then create the server's settings file:
```bash
cp .env.example .env
nano .env
```
Set `MONGO_URI` to the Atlas connection string and `FLASK_SECRET_KEY` to a random value (`python3 -c "import secrets; print(secrets.token_hex(32))"` generates one). Save with **Ctrl+O**, **Enter**, then exit with **Ctrl+X**.

A quick check that the app starts:
```bash
gunicorn --bind 127.0.0.1:8000 app:app &
sleep 2
curl http://127.0.0.1:8000/health        # should print {"status":"ok"}
kill %1
```

## Step 8: Keep the app running with systemd

Running the app as a service means it keeps going after you log out, and comes back on its own if it crashes or the server reboots.

```bash
cd ~/healthcare-survey
pkill gunicorn                              # make sure the test copy isn't still using port 8000
sudo cp deploy/healthcare-survey.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now healthcare-survey
sudo systemctl status healthcare-survey     # should say "active (running)"; press q to leave
```

## Step 9: Put Nginx in front of the app

Gunicorn only listens inside the server on port 8000. Nginx listens on port 80, the normal web port, and passes requests through to it.

```bash
cd ~/healthcare-survey
sudo cp deploy/nginx-healthcare-survey.conf /etc/nginx/sites-available/healthcare-survey
sudo ln -s /etc/nginx/sites-available/healthcare-survey /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t                  # should say the syntax is ok
sudo systemctl restart nginx
```

## Step 10: Try it out

1. Open **http://16.192.107.188**. Use `http`, not `https`; the site doesn't have a certificate, which is also why the browser says "Not secure".
2. Fill in the form and submit. You should see the "Thank you!" page.
3. Refresh the `users` collection in Atlas. The new response is at the bottom.

To update the app after pushing changes to GitHub:
```bash
cd ~/nxu && git pull
cd ~/healthcare-survey && source venv/bin/activate && pip install -r requirements.txt
sudo systemctl restart healthcare-survey
```

## Step 11: Shut it down after grading

1. **EC2 → Instances** → select the instance → **Instance state → Terminate**.
2. **EC2 → Elastic IPs** → select the address → **Actions → Release Elastic IP address**. It keeps costing money until it's released.
3. Optionally delete the Atlas cluster as well.

---

## Things that tripped me up

| What happened | Why, and how I fixed it |
|---|---|
| The browser just timed out on the site's address | Port 80 wasn't open. In the instance's security group, add an inbound rule: **HTTP, port 80, source 0.0.0.0/0**. Also make sure the address starts with `http://`. |
| EC2 Instance Connect: *"Error establishing SSH connection"* | The SSH rule only allowed my IP. Add the `ec2-instance-connect` rule for your region (Step 6). |
| SSH stopped working after I changed location | My home IP isn't fixed. Edit the SSH rule and set the source to **My IP** again. |
| `export_to_csv.py` failed locally with `SSL handshake failed ... tlsv1 alert internal error` | Despite the wording, this means Atlas doesn't recognise your IP. Add your current IP under **Network Access**. |
| The service wouldn't start | A test copy of Gunicorn was still using port 8000. `pkill gunicorn`, then start the service again. |
| **502 Bad Gateway** | Nginx is fine, but the app isn't running. Check `sudo systemctl status healthcare-survey` and `sudo journalctl -u healthcare-survey -n 50`. |
| `bad auth : authentication failed` | Wrong username or password in `MONGO_URI`, or the password has special characters. After fixing `.env`, run `sudo systemctl restart healthcare-survey`. |
| SSH: `UNPROTECTED PRIVATE KEY FILE` | Run the `icacls` command from Step 6. |
| `pip install` failed on Windows with *"Microsoft Visual C++ 14.0 or greater is required"* | I'd made the local venv with Python 3.15, which is too new for some packages. Recreating it with Python 3.11 fixed it. |
| `pip install` failed on Windows with *"No such file or directory"* on a very long path | Windows' 260-character path limit. Turn on long paths (`LongPathsEnabled` in the registry, as admin) or put the venv in a short folder like `C:\venvs\`. |
