class Payment:
    def __init__(self, policyholder, product, amount_due):
        self.policyholder = policyholder
        self.product = product
        self.amount_due = amount_due
        self.status = 'unpaid'

    def process_payment(self, amount_paid):
        if amount_paid >= self.amount_due:
            self.status = 'paid'
            print(f'Payment processed for {self.policyholder.name} on {self.product.name}.')
        else:
            print('Insufficient payment.')

    def apply_penalty(self, penalty_amount):
        self.amount_due += penalty_amount

    def send_reminder(self):
        print(f'Reminder: Payment due for {self.policyholder.name} on {self.product.name}.')
