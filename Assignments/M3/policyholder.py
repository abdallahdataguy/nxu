class Policyholder:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.status = "unregistered"
        self.product = None
        self.total_paid = 0

    def register(self, product):
        if self.status != "unregistered":
            raise ValueError("Member is already registered.")
        if product.status != "active":
            raise ValueError("This product is suspended.")
        self.product = product
        self.status = "active"

    def suspend(self):
        if self.status != "active":
            raise ValueError("You can only suspend active members.")
        self.status = "suspended"

    def reactivate(self):
        if self.status != "suspended" or self.product.status != "active":
            raise ValueError("To reactivate, there must be a suspended member and active product.")
        self.status = "active"

    def display_details(self):
        print("\nMember ID:", self.member_id)
        print("Name:", self.name)
        print("Status:", self.status)
        if self.product is not None:
            print("Product:", self.product.name)
        print(f"Total paid: {self.total_paid:.2f}")
