# Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggieSize(lists):
	for i in range(len(lists)):
		if(lists[i] > 0):
			lists[i] = "big"
	return lists
print("biggieSize: ",biggieSize([-1, 3, -5, -5]))


# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number)

def countPositive(lists):
	count = 0;
	for i in range(len(lists)):
		if(lists[i] > 0):
			count += 1
	lists[len(lists)-1] = count
	return lists

print("countPositive: ",countPositive([1,6,-4,-2,-7,-2]))

# Create a function that takes a list and returns the sum of all the values in the array.

def sumOfArray(lists):
	sum = 0;
	for x in range(len(lists)):
		sum += lists[x]
	return sum

print("sumOfArray: ",sumOfArray([6,3,-2]))

# # Create a function that takes a list and returns the average of all the values.
	
def averageOfArray(lists):
	sum = 0
	for x in range(len(lists)):
		sum += lists[x]
	return sum / len(lists)

print("averageOfArray: ",averageOfArray([1,2,3,4]))

# Create a function that takes a list and returns the length of the list.

def listLength(lists):
	return len(lists)
print("listLength: ",listLength([2,3,4,5,-6]))

# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

def minNum(lists):
	if(len(lists) > 0):
		min = lists[0]
		for x in range(1,len(lists)):
			if(lists[x] < min):
				min = lists[x]
	else:
		return False

	return min

print("minNum: ",minNum([37,2,1,-9]))


# Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.

def maxNum(lists):
	if(len(lists) > 0):
		max = lists[0]
		for x in range(1,len(lists)):
			if(lists[x] > max):
				max = lists[x]
	else:
		return False

	return max

print("maxNum: ",maxNum([]))

# Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimateAnalysis(lists):
	sumTotal = 0
	average = 0
	min = 0
	max = 0
	for x in range(len(lists)):
		if(lists[x] > max):
			max = lists[x]
		if(lists[x] < min):
			min = lists[x]
		sumTotal += lists[x]

	average = sumTotal / len(lists)

	myDict = {'sumTotal': sumTotal, 'average':average,'minimum':min,'maximum':max,'length':len(lists)}

	return myDict

print("ultimateAnalysis: ",ultimateAnalysis([37,2,1,-9]))
		
# Create a function that takes a list and return that list with values reversed. Do this without creating a second list.

def reverseList(lists):
	temp = 0
	for x in range(len(lists) // 2):
		temp = lists[len(lists)-x-1]
		lists[len(lists)-x-1] = lists[x]
		lists[x] = temp
	return lists

print("reverseList: ",reverseList([1,2,3,4,5,6]))





















