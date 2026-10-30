"""Insert randomly generated survey responses into MongoDB for testing.

The analysis charts need a reasonable number of responses to be meaningful.
Use this to populate the database, then add real responses through the form.

Usage:
    python seed_data.py          # inserts 200 responses
    python seed_data.py 500
"""

import random
import sys
from datetime import datetime, timezone

import config
from db import get_collection
from user import User


def random_user():
    age = random.randint(18, 70)
    # Income rises with age until the mid-40s, then levels off.
    base = 1500 + min(age, 45) * 80
    total_income = round(max(500, random.gauss(base, 900)), 2)

    expenses = {}
    for key, _ in config.EXPENSE_CATEGORIES:
        if key == "school_fees" and age > 55:
            continue
        if random.random() < 0.7:
            share = random.uniform(0.03, 0.15)
            expenses[key] = round(total_income * share, 2)

    gender = random.choices(config.GENDERS, weights=[46, 46, 5, 3])[0]
    return User(age, gender, total_income, expenses, submitted_at=datetime.now(timezone.utc))


def seed(n=200):
    docs = [random_user().to_document() for _ in range(n)]
    get_collection().insert_many(docs)
    print(f"Inserted {n} sample responses into {config.MONGO_DB_NAME}.{config.MONGO_COLLECTION}")


if __name__ == "__main__":
    seed(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
