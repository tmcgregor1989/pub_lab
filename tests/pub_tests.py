import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from tests.customer_tests import TestCustomer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Park Bar", 300.00, ["Tennents", "Guinness"])
        self.drink = Drink("wine", 7.50)
        self.drink2 = Drink("vodka", 2.00)
        self.customer = Customer("Trevor", 50, 24)
        self.customer2 = Customer("Jane", 10, 17)
    def test_pub_has_name(self):
        self.assertEqual("The Park Bar", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(3.50)
        self.assertEqual(303.50, self.pub.till)


    def test_sell_drink(self):
      
    
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(42.50, self.customer.wallet)
        self.assertEqual(307.50, self.pub.till)
        
   

    def test_sell_drink_age_check_ok(self):
        self.pub.sell_drink_age_check(self.drink, self.customer)
        self.assertEqual(42.50, self.customer.wallet)
        self.assertEqual(307.50, self.pub.till)

    def test_sell_drink_age_check_too_young(self):
        self.pub.sell_drink_age_check(self.drink, self.customer2)
        self.assertEqual(10.00, self.customer2.wallet)
        self.assertEqual(300.00, self.pub.till)