class Payment:
    def __init__(self, member, due_date):
        if member.status != "active" or member.product.status != "active":
            raise ValueError("Member and product must be active.")
        self.member = member
        self.due_date = due_date
        self.amount = member.product.premium
        self.penalty = 0
        self.penalty_applied = False
        self.paid = False

    def process(self):
        if self.paid:
            raise ValueError("This payment has already been made.")
        if self.member.status != "active" or self.member.product.status != "active":
            raise ValueError("Member and product must be active.")
        total = round(self.amount + self.penalty, 2)
        self.member.total_paid = round(self.member.total_paid + total, 2)
        self.paid = True
        print(f"Payment received from {self.member.name}: {total:.2f}")

    def reminder(self):
        if self.paid:
            print("Payment is complete.")
        else:
            print(f"{self.member.name}, your payment of {self.amount + self.penalty:.2f} "
                  f"is due on {self.due_date}.")

    def apply_penalty(self, today, fee=10):
        if fee < 0:
            raise ValueError("Penalty cannot be negative.")
        if today > self.due_date and not self.paid and not self.penalty_applied:
            self.penalty = fee
            self.penalty_applied = True
            print(f"Late fee added: {fee:.2f}")
