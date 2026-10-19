# Milestone Assignment 1: Policy Management System

This program manages insurance members, products, and payments using three separate classes.

## Run it

Install Python 3, extract the submission ZIP, and open a terminal in that folder. Run:

```sh
python main.py
```

No extra packages are needed.

## Files

- `product.py`: creates, updates, and suspends products.
- `policyholder.py`: registers, suspends, and reactivates members, and displays account details.
- `payment.py`: processes a full payment, displays reminders, and adds a late fee.
- `main.py`: demonstrates the program using two members on the same product.
- `test_policy_system.py`: checks the main rules. Run with `python -m unittest -v`.

## How it works

The demo creates a health product and updates its premium to 120. Amina pays 120. David pays 130 after a late fee of 10. Their account details show their names, IDs, status, product, and total paid. Amina is suspended and reactivated. Finally, the product is suspended, and the program rejects a new registration for it.

To try other details, edit the names, premium, or dates in `main.py`. Create a member with `Policyholder(id, name)`, call `register(product)`, then create a bill with `Payment(member, due_date)`. Call `process()` to mark that bill fully paid.

## Assumptions

Each member has one product. Product suspension keeps the record but prevents new registrations and payments. Suspended members cannot pay. A payment covers the full bill; partial payments are not included. Calling `process()` twice on the same payment is rejected. Product price changes do not change an existing bill.

The assignment does not give a penalty rule. This example uses a flat fee of 10, applied once to an unpaid overdue bill when `apply_penalty(today)` is called. Pass a second argument to choose a different fee. Dates in the demo are fixed so the result stays the same each time.

Reminders are printed, not sent. Amounts use ordinary Python numbers for this classroom example. Records stay in memory and are lost when the program closes. There is no database or actual payment service.

Submit `Milestone_Assignment_1_Submission.zip`. No GitHub upload has been performed.
