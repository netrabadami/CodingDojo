def insertionSort(myList): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(myList)): 
  
        key = myList[i] 
        j = i-1
        while j >= 0 and key < myList[j] : 
                myList[j + 1] = myList[j] 
                j -= 1
        myList[j + 1] = key 
        print("myList",myList)

    return myList

print("insertionSort",insertionSort([6,5,1,3]))