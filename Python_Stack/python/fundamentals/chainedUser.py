class User:
	def __init__(self,userName,emailId):
		self.name = userName
		self.email = emailId
		self.balance = 200

	def deposite(self,amount):
		self.balance += amount
		return self.balance

	def make_withdrawal(self,amount):
		self.balance -= amount
		return self.balance

	def display_user_balance(self):
		return "user :",self.name,"balance :",self.balance

	def transfer_money(self, other_user, amount):
		less = self.make_withdrawal(amount)
		bonus = other_user.deposite(amount)
		return less,bonus


testUser1 = User("user1","user1@abc.com")
testUser2 = User("user2","user2@abc.com")




print("test chaining",testUser1.make_withdrawal(50).deposite(100))
# print("with draw",testUser1.make_withdrawal(10))
# print("Display ",testUser1.display_user_balance())
# print("BONUS ",testUser1.transfer_money(testUser2,20))