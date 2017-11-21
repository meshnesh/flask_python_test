import unittest

from bank_account import BankAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_yangu = BankAccount() #meaning is where my error is

    def test_login(self):
        self.assertEqual(self.account_yangu.name, "Phil_johnes", msg='wrong username')
        self.assertEqual(self.account_yangu.password, "qwerty1234", msg='wrong password')