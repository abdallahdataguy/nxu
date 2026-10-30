"""The User class: one survey participant and their income/expense data."""

from config import EXPENSE_CATEGORIES

CATEGORY_KEYS = [key for key, _ in EXPENSE_CATEGORIES]


class User:
    """A survey participant.

    Expenses are stored as a dict of {category: amount}. Categories the
    participant did not tick are recorded as 0 so every row in the CSV has
    the same columns.
    """

    CSV_HEADERS = ["age", "gender", "total_income", *CATEGORY_KEYS, "total_expenses"]

    def __init__(self, age, gender, total_income, expenses=None, submitted_at=None):
        self.age = int(age)
        self.gender = str(gender)
        self.total_income = float(total_income)
        expenses = expenses or {}
        self.expenses = {key: float(expenses.get(key, 0) or 0) for key in CATEGORY_KEYS}
        self.submitted_at = submitted_at

    @property
    def total_expenses(self):
        return round(sum(self.expenses.values()), 2)

    @classmethod
    def from_document(cls, doc):
        """Build a User from a MongoDB document."""
        return cls(
            age=doc["age"],
            gender=doc["gender"],
            total_income=doc["total_income"],
            expenses=doc.get("expenses", {}),
            submitted_at=doc.get("submitted_at"),
        )

    def to_document(self):
        """Return the dict stored in MongoDB."""
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "expenses": self.expenses,
            "submitted_at": self.submitted_at,
        }

    def to_csv_row(self):
        """Return a dict keyed by CSV_HEADERS."""
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            **self.expenses,
            "total_expenses": self.total_expenses,
        }

    def __repr__(self):
        return (
            f"User(age={self.age}, gender={self.gender!r}, "
            f"total_income={self.total_income}, total_expenses={self.total_expenses})"
        )
