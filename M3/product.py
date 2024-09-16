class Product:
    def __init__(self, name, coverage, price):
        self.name = name
        self.coverage = coverage
        self.price = price

    def update(self, new_name=None, new_coverage=None, new_price=None):
        if new_name:
            self.name = new_name
        if new_coverage:
            self.coverage = new_coverage
        if new_price:
            self.price = new_price

    def __repr__(self):
        return f'{self.name} - {self.coverage} at {self.price}'
