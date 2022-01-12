import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("John Doe", 100.00, 18)

    def test_customer_has_name(self):
        self.assertEqual("John Doe", self.customer.name)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(3.50)
        self.assertEqual(96.50, self.customer.wallet)

