class Customer:
    def __init__(self, name):
        self.name = name
        self.drinks = []

    def get_name(self):
        return self.name

    def get_drinks(self):
        return self.drinks

    def set_name(self, name):
        self.name = name

    def set_drinks(self, drinks):
        self.drinks = drinks

    def add_drink(self, drink):
        self.drinks.append(drink)
