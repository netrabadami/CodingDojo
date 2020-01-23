class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class SLL:
	def __init__(self):
		self.head = None


	def insertFront(self,value):
		newNode = Node(value)
		currHead = self.head
		if currHead == None:
			self.head = newNode
			self.next = None
		else:
			self.head = newNode
			newNode.next = currHead
		return self

	def insertLast(self,value):
		newNode = Node(value)
		currHead = self.head
		if currHead == None:
			self.head = newNode
			newNode.next = None
		else:
			while currHead.next != None:
				currHead = currHead.next
			currHead.next = newNode
			newNode.next = None
		return self

	def removeFront(self):
		currHead = self.head
		if currHead != None:
			self.head = currHead.next
		else:
			self.head = None
			print("list is empty")
		return self
			

	def removelast(self):
		currHead = self.head
		prev = currHead
		if currHead == None or currHead.next == None:
			self.head = None
		else:
			while currHead.next != None:
				prev = currHead
				currHead = currHead.next
			prev.next = None
		return self

	def count(self):
		count = 0
		currHead = self.head
		while currHead != None:
			count += 1
			currHead = currHead.next
		print("count",count)
		return count

	def insertMid(self,value):
		newNode = Node(value)
		count = 0
		currHead = self.head
		runner = self.head
		newCount = 0
		while currHead != None:
			count += 1
			currHead = currHead.next
		print("countttt",count)
		midPoint = count / 2
		print("midpoint",midPoint)
		# if currHead == None:
		# 	print("efrerferfer")
		# 	self.head = newNode
		# 	return self
		# else:
		while runner.next != None:
			newCount += 1
			print("newCount",newCount)
			if newCount ==  midPoint:
				print("meets",runner.value)
				newNode.next = runner.next
				runner.next = newNode
				return self
			runner = runner.next

	def printList(self):
		currHead = self.head
		while currHead != None:
			print(currHead.value)
			currHead = currHead.next
		return self


myList = SLL()
# myList.insertFront(1).printList()
print("Insert front")
myList.insertFront(2).printList()
myList.insertLast(3)
myList.insertLast(4)
myList.insertLast(5).printList()
# myList.count()
# print("remove front")
# myList.removeFront().printList()
# print("remove again")
# myList.removeFront().printList()
# print("remove from last")
# myList.removelast().printList()
myList.insertMid(6).printList()
















