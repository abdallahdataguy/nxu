# Module 3 Assignment: Policy Management System
This repository has two files, Jupyter notebook Python file and R script.

## Overview
- This project is a simple Policy Management System for an insurance company. It manages policyholders, products, and payments. Policy managers can perform various tasks, such as adding and suspending policyholders, registering new members, and managing policy products. Payments can also be processed, and reminders can be sent to policyholders.

## Features
1. Policyholder Management: Allows registering, suspending, and reactivating policyholders.
2. Product Management: Enables creating, updating, and suspending insurance products.
3. Payment Management: Handles payment processing, sends payment reminders, and applies penalties for late payments.
4. Demonstration: Demonstrates the functionality of the system by creating two policyholders, registering them for a product, and processing their payments.

## Prerequisites
- Ensure that you have Python installed on your machine. You can check if Python is installed on your machine and the installed version by running the following command on command terminal (e.g. command prompt or Windows PowerShell in a Windows PC):
- `python --version`

## Installation
1. Clone this repository or download the ZIP file.
2. Extract the contents (if downloading the ZIP).
3. Ensure that the following files are in the same directory:
- policyholder.py
- product.py
- payment.py
- main.py
- README.md

## Running the Project
- To run the project, navigate to the directory containing the files and execute the following command in your terminal:
- `python main.py`
- Alternatively, you can open the file `main.py` in a Python IDE of your choice such as the built-in IDLE and run the module (F5 keyboard shortcut in IDLE)
- This will create two policyholders, register them for insurance products, process their payments, and display their account details.

## File Descriptions
1. policyholder.py: Contains the Policyholder class, which manages policyholder information and their status.
2. product.py: Contains the Product class, which defines insurance products.
3. payment.py: Contains the Payment class, which processes payments and manages reminders and penalties.
4. main.py: Demonstrates the functionality by creating policyholders, registering them for products, processing payments, and displaying account details.