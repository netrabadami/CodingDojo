class BankAccount:
	def __init__(self, int_rate, balance = 0): # don't forget to add some default values for these parameters!
		self.int_rate = 0.01
		self.balance = balance

	def deposit(self, amount):
		self.balance +=amount
		return self.balance
		# your code here
	def withdraw(self, amount):
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


testUser1 = BankAccount(1,1000)
print("Balance after deposite", testUser1.deposit(200))
print("Balance after withdraw", testUser1.withdraw(300))
print("Balance after adding intrest", testUser1.yield_interest())	


