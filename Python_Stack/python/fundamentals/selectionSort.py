def selectionSort(myList):
	n = len(myList)
	for i in range(n):
		idx = i
		for j in range(i+1,n):
			if(myList[idx] > myList[j]):
				idx=j
		myList[i], myList[idx] = myList[idx], myList[i] 
		print("myList",myList)

	return myList

print("selectionSort",selectionSort([6,5,1,3]))