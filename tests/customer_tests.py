import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("John Doe", 100.00, 18, 3)

    def test_customer_has_name(self):
        self.assertEqual("John Doe", self.customer.name)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(3.50)
        self.assertEqual(96.50, self.customer.wallet)

    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(3)
        self.assertEqual(6, self.customer.drunkenness)