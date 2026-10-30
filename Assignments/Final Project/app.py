"""Flask survey app that collects participants' income and spending data."""

from datetime import datetime, timezone

from flask import Flask, flash, redirect, render_template, request, url_for

import config
from db import get_collection
from user import User

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


def parse_form(form):
    """Validate the submitted form. Returns (User, errors)."""
    errors = []

    try:
        age = int(form.get("age", ""))
        if not 1 <= age <= 120:
            errors.append("Age must be between 1 and 120.")
    except ValueError:
        age = None
        errors.append("Please enter a valid age.")

    gender = form.get("gender", "")
    if gender not in config.GENDERS:
        errors.append("Please select a gender.")

    try:
        total_income = float(form.get("total_income", ""))
        if total_income < 0:
            errors.append("Total income cannot be negative.")
    except ValueError:
        total_income = None
        errors.append("Please enter a valid total income.")

    expenses = {}
    for key, label in config.EXPENSE_CATEGORIES:
        if not form.get(f"category_{key}"):
            continue
        try:
            amount = float(form.get(f"amount_{key}", ""))
            if amount < 0:
                errors.append(f"{label} amount cannot be negative.")
            expenses[key] = amount
        except ValueError:
            errors.append(f"Please enter an amount for {label}.")

    if errors:
        return None, errors
    user = User(age, gender, total_income, expenses, submitted_at=datetime.now(timezone.utc))
    return user, []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user, errors = parse_form(request.form)
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "index.html",
                categories=config.EXPENSE_CATEGORIES,
                genders=config.GENDERS,
                form=request.form,
            ), 400
        get_collection().insert_one(user.to_document())
        return redirect(url_for("thank_you"))

    return render_template(
        "index.html",
        categories=config.EXPENSE_CATEGORIES,
        genders=config.GENDERS,
        form={},
    )


@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
