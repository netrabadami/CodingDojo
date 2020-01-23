def bubbleSort(myList):
	for i in range(len(myList)):
		for j in range(0,len(myList)-i-1):
			if(myList[j] > myList[j+1]):
				myList[j], myList[j+1] = myList[j+1] , myList[j]

	return myList


print("bubbleSort",bubbleSort([6,3,1,5]))