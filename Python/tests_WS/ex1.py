# Approved by: Arin

import unittest

class BankAccount():
    """ Class of bank account with option to deposit and withdraw """
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount
        return True


class TestBankAccount(unittest.TestCase):
    """ Tests running on BankAccount class """
    def setUp(self):
        self.account = BankAccount(123456789)
    
    def test_init_balance(self):
        self.assertEqual(self.account.balance, 0, "New account's balance should be initialized to 0.")

    def test_deposit(self):
        self.assertGreater(self.account.deposit(1000), 0, "Deposit amount should be greater then 0.")
        self.assertEqual(self.account.balance, 1000, "Balance should be 1000 after deposit.")
    
    def test_withdraw_success(self):
        self.account.deposit(1000)
        self.assertTrue(self.account.withdraw(300), "Deposit 1000 and Withdraw 300 should return true.")
        self.assertEqual(self.account.balance, 700, "Balance after withdrawal should be 700.")
    
    def test_withdraw_fail(self):
        self.account.deposit(1000)
        self.assertFalse(self.account.withdraw(2000), "Withdraw 2000 from 1000 should return false.")
        self.assertEqual(self.account.balance, 1000, "Balance should remain 1000 after failed withdrawal.")

    def tearDown(self):
        self.account = None
        self.assertIsNone(self.account, "Account should not be exist after closing.")


if __name__ == '__main__':
    unittest.main()