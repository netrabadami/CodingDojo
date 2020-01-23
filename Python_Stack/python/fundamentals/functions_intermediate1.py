import random

def randInt(min=0,max=100):
	return random.random() * max


print("print random default: ",randInt())
print("print random max: ",randInt(max=50))
print("print random min: ",randInt(min=50))
print("print random min and max: ",randInt(min=50,max=500))