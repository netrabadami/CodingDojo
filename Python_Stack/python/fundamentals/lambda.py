def map(myList,fun):
	for i in range(len(myList)):
		x = fun(myList[i])
		print(x)

print(map([1,2,3,4],lambda n: n*2))