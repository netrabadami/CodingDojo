class MathDojo:
	def __init__(self):
		self.result = 0

	def add(self,num1,num2):
		self.result = num1 + num2
		return self.result

			

	def subtract(self, num1,*nums):
		pass

md = MathDojo()

print(md.add(2,4))