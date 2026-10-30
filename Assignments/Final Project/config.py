"""Central configuration, read from environment variables (or a .env file)."""

import os

from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "healthcare_survey")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "users")
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-only-change-me")

# Expense categories offered on the survey form: (form/database key, label shown to the user)
EXPENSE_CATEGORIES = [
    ("utilities", "Utilities"),
    ("entertainment", "Entertainment"),
    ("school_fees", "School Fees"),
    ("shopping", "Shopping"),
    ("healthcare", "Healthcare"),
]

GENDERS = ["Male", "Female", "Non-binary", "Prefer not to say"]
