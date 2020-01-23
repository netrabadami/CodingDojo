class User:
	def __init__(self,userName,emailId):
		self.name = userName
		self.email = emailId
		self.account = BankAccount(int_rate=0.02,balance=0,accNumber=1)
		# self.balance = 200

	def make_deposite(self,amount, accNumber):
		deposite = self.account.deposite(amount,1)
		return deposite


	def make_withdrawal(self,amount, accNumber):
		withdraw = self.account.withdraw(amount,1)
		return withdraw

	def display_info(self):
		return "user :",self.name,"balance :",self.account.balance

	# def transfer_money(self, other_user, amount):
	# 	less = self.make_withdrawal(amount)
	# 	bonus = other_user.deposite(amount)
	# 	return less,bonus

class BankAccount:
	def __init__(self, int_rate, balance = 0, accNumber=1): # don't forget to add some default values for these parameters!
		self.int_rate = 0.01
		self.balance = balance
		self.accNumber = accNumber

	def deposite(self, amount, accNumber):
		self.balance +=amount
		return self.balance
		# your code here
	def withdraw(self, amount, accNumber):
		if(self.balance > amount):
			self.balance -=amount
			return self.balance
		else:
			return "Insufficient funds: Charging a $5 fee and deduct $5"

	def display_account_info(self):
		print("Balance: ",self.balance)

	def yield_interest(self):
		if(self.balance > 0):
			self.balance = self.balance + (self.balance * self.int_rate)
		return self.balance


testUser1 = User("user1","user1@abc.com")

print("association of class", testUser1.make_deposite(100,2))
print("with draw",testUser1.make_withdrawal(10,2))
print("Display ",testUser1.display_info())
# print("BONUS ",testUser1.transfer_money(testUser2,20))