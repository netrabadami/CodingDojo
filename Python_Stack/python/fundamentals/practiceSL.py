class SLNode:
	def __init__(self,value,idx):
		self.val = value
		self.next = None
		self.idx = idx

class SList:
	def __init__(self):
		self.head = None

	def addToFront(self,val,idx):
		newNode = SLNode(val,idx)
		currentHead = self.head
		newNode.next = currentHead
		self.head = newNode
		return self

	# def addtoBack(self,val):
	# 	newNode = SLNode(val)
	# 	currentHead = self.head
	# 	while (currentHead.next != None):
	# 		currentHead = currentHead.next
	# 	currentHead.next = newNode
	# 	print("length of List")
	# 	return self

	# def removeFromFront(self):
	# 	currentHead = self.head
	# 	self.head = currentHead.next
	# 	return self

	# def removeFromback(self):
	# 	currentHead = self.head
	# 	while (currentHead.next != None):
	# 		prevHead = currentHead
	# 		currentHead = currentHead.next
	# 	prevHead.next = currentHead.next
	# 	return self

	# def remove(self,val):
	# 	currentHead = self.head
	# 	# remove from first node
	# 	if(currentHead.val == val):
	# 		self.head = currentHead.next
	# 	else:
	# 		prevHead = currentHead
	# 		while (currentHead.next !=None):
	# 			if(currentHead.val == val):
	# 				break
	# 			prevHead = currentHead
	# 			currentHead = currentHead.next
	# 		prevHead.next = currentHead.next		
	# 	return self

	def insertVal(self,val,idx):
		currentHead = self.head
		if idx == 0:
			print("seldfsedhef")
			newNode = SLNode(val,idx)
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
myList.addToFront("Patil",0).addToFront("Netra",1).addToFront("Badami",1).addToFront("Chetan",1).printList()
# print("remove from front")
# myList.removeFromFront().printList()
# print("remove from back")
# myList.removeFromback().printList()
# print("remove val")
# myList.remove("Netra").printList()
# print("list count ")
# myList.insertVal("name",2)
print("insert val")
myList.insertVal("USA",0).printList()

