class Menu:
    def __init__(self, drinks):
        self.drinks = drinks

    def set_drinks(self, drinks):
        self.drinks = drinks

    def get_drinks(self):
        return self.drinks

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.discard(drink)
