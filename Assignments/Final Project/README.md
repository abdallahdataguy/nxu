# Healthcare Spending Survey: Flask + MongoDB + Python Analysis

BAN6420 Final Project. A survey tool that collects participants' age, gender, income and spending, stores the responses in MongoDB, exports them to CSV through a `User` class, and analyses them in a Jupyter notebook. The analysis supports a new healthcare product launch.

**Live app:** `http://<your-elastic-ip>` *(replace this after deploying; see [AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md))*

## How the requirements are met

| Requirement | Where |
|---|---|
| Flask webpage to collect user data | [app.py](app.py), [templates/index.html](templates/index.html) |
| Store Age, Gender, Total Income and Expenses in MongoDB | [app.py](app.py) (`insert_one`), [db.py](db.py) |
| Checkboxes for utilities, entertainment, school fees, shopping and healthcare, each with an amount textbox | [templates/index.html](templates/index.html) |
| Python class named `User` | [user.py](user.py) |
| Loop through the collected data and store it in a CSV file | [export_to_csv.py](export_to_csv.py) → `data/user_data.csv` |
| Load the CSV into a Jupyter notebook | [analysis.ipynb](analysis.ipynb) |
| Chart: ages with the highest income | notebook section 3 → `charts/01_*.png`, `charts/02_*.png` |
| Chart: gender distribution across spending categories | notebook section 4 → `charts/03_*.png`, `charts/04_*.png` |
| Export charts for PowerPoint | 300-dpi PNGs saved to `charts/` |
| Host on AWS | EC2 + Gunicorn + Nginx, data in MongoDB Atlas: [AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md), [deploy/](deploy/) |

## Project structure

```
Final Project/
├── app.py                    # Flask app: survey form, validation, save to MongoDB
├── config.py                 # Settings from .env; expense categories and gender options
├── db.py                     # MongoDB connection helper
├── user.py                   # The User class
├── export_to_csv.py          # Loops through MongoDB → User objects → data/user_data.csv
├── seed_data.py              # Inserts random sample responses (for testing the charts)
├── analysis.ipynb            # Jupyter notebook: loads CSV, cleans data, makes and exports charts
├── templates/                # HTML pages (base, survey form, thank-you)
├── static/style.css          # Page styling
├── deploy/                   # systemd service + Nginx config for the AWS server
├── requirements.txt          # Web app dependencies
├── requirements-analysis.txt # + pandas, matplotlib, seaborn, Jupyter
├── .env.example              # Template for environment variables
├── AWS_DEPLOYMENT.md         # Step-by-step AWS hosting guide
├── data/                     # (created by export_to_csv.py)
└── charts/                   # (created by the notebook)
```

## Running it locally

### 1. Prerequisites
- Python 3.10 or newer
- MongoDB: either
  - **MongoDB Atlas** (free cloud database, also used for the AWS deployment; Step 1 of [AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md)), or
  - **MongoDB Community Server** installed locally: <https://www.mongodb.com/try/download/community>

### 2. Install

```bash
python -m venv venv
# Windows:      venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate
pip install -r requirements-analysis.txt
```

### 3. Configure
Copy `.env.example` to `.env` and set `MONGO_URI`:
- Local MongoDB: `mongodb://localhost:27017/`
- Atlas: `mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority`

### 4. Run the web app
```bash
python app.py
```
Open <http://127.0.0.1:5000>, fill in the form and submit.
- Tick a checkbox to enable its amount box.
- Unticked categories are saved as `0`.
- Invalid input (missing age, negative amounts, a ticked category with no amount) is rejected with a message.

### 5. (Optional) Add sample data
The charts need a reasonable number of responses. To add 200 random test responses:
```bash
python seed_data.py 200
```

### 6. Export to CSV
```bash
python export_to_csv.py
```
This loops through every document in MongoDB, converts each one to a `User` object, and writes `data/user_data.csv` with these columns:

`age, gender, total_income, utilities, entertainment, school_fees, shopping, healthcare, total_expenses`

### 7. Analyse in Jupyter
```bash
jupyter notebook analysis.ipynb
```
Run all cells (**Run → Run All Cells**). The charts appear in the notebook and are saved to `charts/`. To use them in PowerPoint, choose **Insert → Pictures → This Device** and pick the PNG files.

## The `User` class

[user.py](user.py) represents one participant:

- **Attributes:** `age`, `gender`, `total_income`, `expenses` (a dict of category → amount, with 0 for unticked categories), `submitted_at`
- **`total_expenses`:** a property giving the sum of all expenses
- **`User.from_document(doc)`:** builds a `User` from a MongoDB document
- **`to_document()`:** returns the dict that is saved to MongoDB
- **`to_csv_row()`:** returns one CSV row, keyed by `User.CSV_HEADERS`

The Flask app uses `User` to build each record before saving it. `export_to_csv.py` uses it to turn each MongoDB document into a CSV row.

## Data stored in MongoDB

Database `healthcare_survey`, collection `users`:

```json
{
  "age": 34,
  "gender": "Female",
  "total_income": 4200.0,
  "expenses": {
    "utilities": 300.0, "entertainment": 0.0, "school_fees": 0.0,
    "shopping": 0.0, "healthcare": 150.0
  },
  "submitted_at": "2026-10-30T01:05:09Z"
}
```

## AWS deployment

See **[AWS_DEPLOYMENT.md](AWS_DEPLOYMENT.md)** for full step-by-step instructions: MongoDB Atlas setup, EC2 launch, Gunicorn + systemd, Nginx, testing, troubleshooting and clean-up.
