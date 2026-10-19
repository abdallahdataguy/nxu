class Product:
    def __init__(self, product_id, name, premium):
        if premium <= 0:
            raise ValueError("Premium must be above zero.")
        self.product_id = product_id
        self.name = name
        self.premium = premium
        self.status = "active"

    def update(self, name, premium):
        if premium <= 0:
            raise ValueError("Premium must be above zero.")
        self.name = name
        self.premium = premium

    def suspend(self):
        self.status = "suspended"
