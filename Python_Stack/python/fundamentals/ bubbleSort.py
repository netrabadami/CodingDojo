def bubbleSort(myList):
	for i in range(len(myList)):
		if(myList[i] > myList[i+1]):
			myList[i], myList[i+1] = myList[i+1] , myList[i]
	return myList


print("bubbleSort",bubbleSort([6,3,1,5]))