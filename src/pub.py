from src.customer import Customer
from src.drink import Drink

class Pub:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = []


    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, drink, customer):
        customer.decrease_wallet(drink.price)
        self.increase_till(drink.price)


      

        


