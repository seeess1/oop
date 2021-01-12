"""
An example class to keep track of a customer's biographical and account information.

Then a Tester class at the bottom that uses unittest to make sure things are working as expected.
"""

import unittest

class Account:
	def __init__(self, customer_name, customer_dob, starting_balance=0):
		self.customer_name = customer_name
		self.customer_dob = customer_dob
		self.balance = starting_balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			return self.balance

	def withdrawal(self, amount):
		if amount < 0:
			self.balance += amount
			return self.balance

	def balance_check(self):
		return "Current balance: {}".format(self.balance)

class Tester(unittest.TestCase):

	def setUp(self):
		self.c = Account("Alex", "01/01/1990", 10)
		print(self.c.customer_name)

	def test_customer(self):		
		self.assertEqual(self.c.customer_name, "Alex")
		self.assertEqual(self.c.customer_dob, "01/01/1990")

	def test_balance(self):
		self.c.deposit(100)
		self.assertEqual(self.c.balance, 110)

if __name__ == "__main__":
	unittest.main()