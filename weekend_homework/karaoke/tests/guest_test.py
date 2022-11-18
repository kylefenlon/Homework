import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 200, "One day like this")

    def test_customer_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_customer_has_cash(self):
        self.assertEqual(200, self.guest.cash)

    def test_customer_has_fav_song(self):
        self.assertEqual("One day like this", self.guest.fav_song)

    def test_reduce_cash(self):
        self.guest.reduce_cash(10)
        self.assertEqual(190, self.guest.cash)