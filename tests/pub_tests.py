import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from tests.customer_tests import TestCustomer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Park Bar", 300.00, ["Tennents", "Guinness"])
        self.drink1 = Drink("wine", 7.50)
        self.drink2 = Drink("vodka", 2.00)
        self.customer = Customer("Trevor", 50, 24)
    def test_pub_has_name(self):
        self.assertEqual("The Park Bar", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(3.50)
        self.assertEqual(303.50, self.pub.till)


    def test_sell_drink(self):
        customer = Customer("John", 100, 56)
        drink = Drink("whisky", 5)
    
        self.pub.sell_drink(drink, customer)
        self.assertEqual(95, customer.wallet)
        self.assertEqual(305, self.pub.till)
        
    def test_check_customer_age(self):
        customer = Customer("john", 100, 56)

        self.pub.check_customer_age(customer)
        self.assertEqual