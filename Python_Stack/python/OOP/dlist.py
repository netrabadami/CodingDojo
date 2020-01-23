class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self,val):
        newNode = Node(val)
        currentHead = self.head
        if (currentHead == None):
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            while currentHead.next != None:
                currentHead = currentHead.next
            newNode.next = None
            currentHead.next = newNode
        return self
    
    def addToFront(self,val):
        newNode = Node(val)
        currentHead = self.head
        if (currentHead == None):
            print("in if")
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            if currentHead.prev == None:
                self.head = newNode
                newNode.next = currentHead
            else:
                newNode.prev = currentHead.prev
                currentHead.prev.next = newNode
                currentHead.prev = newNode
        return self

    def removeFromBack(self):
        currentHead = self.head
        if currentHead.prev == None:
            self.head = None
            self.tail = None
        else:
            while currentHead.next != None:
                prevHead = currentHead
                currentHead = currentHead.next
            prevHead.next = None
        return self

    def removeFromFront(self):
        currentHead = self.head
        if currentHead.next == None:
            print("in if")
            self.head = None
            self.tail = None
        else:
            print("in else")
            self.head = currentHead.next
        return self

    def printList(self):
        currentHead = self.head
        while currentHead != None:
            print(currentHead.val)
            currentHead = currentHead.next
        return self



myList =DList()
# myList.addToFront(1).printList()
print("Add Back")
myList.addToBack(1).printList()
# print("Add Back")
# myList.addToBack(2).printList()
# print("Add to Back again")
# myList.addToBack(3).printList()
# print("Add to Back againnnn")
# myList.addToBack(4).printList()
# print("add Front")
# myList.addToFront(3).printList()
# print("add front again")
# myList.addToFront(4).printList()
# print("add front againnnnnnn")
# myList.addToFront(6).printList()
# print("check")
# myList.addToFront(7).printList()
# print("remove last element")
# myList.removeFromBack().printList()
print("remove first element")
myList.removeFromFront().printList()