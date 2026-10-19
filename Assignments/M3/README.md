# Milestone Assignment 1: Policy Management System

This program creates a policy management system for an insurance company that facilitates managing insurance members, products, and payments. It uses thee three different classes to achieve that. 

## Run it

- Install Python 3.x
- Put all files in the same folder, open a terminal in that folder and Run the main python file:

```sh
python main.py
```
- No additional packages are needed to run this program. It uses standard python installation

## Files

- `product.py`: facilitates management of products. It implements a class for working with products like creating, updating and suspending them.
- `policyholder.py`: this file facilites managing members by enabling registering, suspending, and reactivation of members, and also displaying account details.
- `payment.py`: facilitates processing full payments, displaying reminders, and adding late fees.
- `main.py`: program demonstration Python file that uses two members on the same product to perform that demo of the program features.

## How it works

The demo creates a health product first and then set its premium as 120. Amina pays 120 and and David pays 130 after a late penalty which is 10. Their account details show names, IDs, statuses and products including total paid. Amina is suspended and then reactivated. The product is finally suspended and the program then rejects a new registration for the same due to that status.

Try playing with this program by changing details in the main.py file such as late fees, add new members, products and amounts and see how it behaves.

Reminders are not sent but rather just printed. In this demo, amounts use ordinary Python numbers.
