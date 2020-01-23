# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
	numList = [];
	for i in range(num,-1,-1):
		numList.append(i);
	return numList;

print("The new list:",countdown(5));


#  Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def printAndReturn(lists):
	print("Print first number: ",lists[0]);
	return(lists[1]);
print("Return second number: ",printAndReturn([4,8]));

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firdstPlusLength(lists):
	return(lists[0]+len(lists))

print("Return firdstPlusLength: ",firdstPlusLength([1,2,3,4,5,6]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def greaterThanSecond(lists):
	newList =[];
	for i in lists:
		if(i > lists[1]):
			newList.append(i);
			# print("i is: ",i)
	return newList

print("greaterThanSecond: ",greaterThanSecond([2,5,8,3]))


# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is 
# equal to the given size, and whose values are all the given value.

def lengthAndValue(length,val):
	newList = [];
	for i in range(length):
		newList.append(val)
	return newList

print("lengthAndValue: ",lengthAndValue(6,8))






















