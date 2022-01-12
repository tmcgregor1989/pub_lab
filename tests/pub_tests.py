import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from tests.customer_tests import TestCustomer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Park Bar", 300.00, ["Tennents", "Guinness"])

    def test_pub_has_name(self):
        self.assertEqual("The Park Bar", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(3.50)
        self.assertEqual(303.50, self.pub.till)


    def test_sell_drink(self):
        customer = Customer("John", 100)
        drink = Drink("whisky", 5)
    
        self.pub.sell_drink(drink, customer)
        self.assertEqual(95, customer.wallet)
        self.assertEqual(305, self.pub.till)
        