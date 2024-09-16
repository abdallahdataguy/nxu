class Policyholder:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.status = 'active'
        self.policies = []
    
    def register(self, product):
        self.policies.append(product)
    
    def suspend(self):
        self.status = 'suspended'
    
    def reactivate(self):
        self.status = 'active'

    def display_details(self):
        print(f'Policyholder: {self.name}, Status: {self.status}, Policies: {self.policies}')
