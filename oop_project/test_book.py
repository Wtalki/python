import unittest 
from banking_system import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_account_creation(self):
        account = BankAccount("12345","zaw lay",1000)
        self.assertEqual(account.balance,1000)
        self.assertEqual(account.account_holder,"zaw lay")
        self.assertEqual(account.account_number,"12345")
        self.assertEqual(len(account.transaction_history),0)
    
    def test_deposit(self):
        account = BankAccount("12345", "Alice", 1000)
        result = account.deposit(500)
        self.assertEqual(account.balance, 1500)
        self.assertIn("Deposited: $500", account.transaction_history)

        
if __name__ == "__main__":
    unittest.main()