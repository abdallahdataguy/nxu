"""Loop through every survey response in MongoDB and write it to a CSV file.

Usage:
    python export_to_csv.py                 # writes data/user_data.csv
    python export_to_csv.py my_output.csv
"""

import csv
import sys
from pathlib import Path

from db import get_collection
from user import User

DEFAULT_OUTPUT = Path(__file__).parent / "data" / "user_data.csv"


def export_users(output_path=DEFAULT_OUTPUT):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=User.CSV_HEADERS)
        writer.writeheader()
        for doc in get_collection().find():
            user = User.from_document(doc)
            writer.writerow(user.to_csv_row())
            count += 1

    print(f"Exported {count} users to {output_path}")
    return count


if __name__ == "__main__":
    export_users(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT)
