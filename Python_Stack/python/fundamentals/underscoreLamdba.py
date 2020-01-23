class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
        	iterable[i]=callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
    	great = 0
    	for i in range(len(iterable)):
    		if(callback(iterable[i])):
    			great = iterable[i]
    			return great
    def filter(self, iterable, callback):
    	l1 = []
    	for i in range(len(iterable)):
    		if(callback(iterable[i])):
    			l1.append(iterable[i])
    	return l1
    #     # your code
    def reject(self, iterable, callback):
    	l1 = []
    	for i in range(len(iterable)):
    		if not (callback(iterable[i])):
    			l1.append(iterable[i])
    	return l1
    #     # your code
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)




multiple = _.map([1,2,3], lambda x: x*2)
print(multiple) # should return [2,4,6]
greater = _.find([1,2,3,4,5,6], lambda x: x>4) 
print(greater) # should return the first value that is greater than 4
evens = _.filter([1,2,3,4,5,6], lambda x: x%2==0) 
print(evens) # should return [2,4,6]
reject = _.reject([1,2,3,4,5,6], lambda x: x%2==0) 
print(reject) #should return [1,3,5]
