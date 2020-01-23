class SLNode:
	def __init__(self,value):
		self.val = value
		self.next = None

class SList:
	def __init__(self):
		self.head = None

	# Creates new node and adds to front
	def addToFront(self,val):
		newNode = SLNode(val)
		currentHead = self.head
		newNode.next = currentHead
		self.head = newNode
		return self

	def printList(self):
		runner = self.head
		while (runner != None):
			print(runner.val)
			runner = runner.next
		return self

myList = SList()
myList.addToFront("Chetan").addToFront("Badami").printList()

