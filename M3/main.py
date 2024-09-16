from policyholder import Policyholder
from product import Product
from payment import Payment

# Create Products
product1 = Product(name='Health Insurance', coverage='Comprehensive', price=500)
product2 = Product(name='Life Insurance', coverage='Full Coverage', price=300)

# Create Policyholders
policyholder1 = Policyholder(name='John Doe', address='123 Elm Street')
policyholder2 = Policyholder(name='Jane Smith', address='456 Oak Avenue')

# Register Policyholders to a Product
policyholder1.register(product1)
policyholder2.register(product2)

# Process Payments for Both Policyholders
payment1 = Payment(policyholder=policyholder1, product=product1, amount_due=500)
payment1.process_payment(500)

payment2 = Payment(policyholder=policyholder2, product=product2, amount_due=300)
payment2.process_payment(300)

# Display Policyholder Details
print('\nPolicyholder 1 Details:')
policyholder1.display_details()

print('\nPolicyholder 2 Details:')
policyholder2.display_details()
