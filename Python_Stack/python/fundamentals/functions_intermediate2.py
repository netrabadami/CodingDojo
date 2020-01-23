x = [ [5,2,3], [10,8,9] ] 
student = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# print(x)

# #Change the last_name of the first student from 'Jordan' to 'Bryant'
student[0]['last_name'] = 'Bryant'
# print(students)

# # In the sports_directory, change 'Messi' to 'Andres'
# print(sports_directory['soccer'][1])
for key,val in sports_directory.items():
	for x in range(len(val)):
		if(val[x] == "Messi"):
			val[x] = "Andres"
				
print(sports_directory)

# # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# Iterate Through a List of Dictionaries
def iterateDictionary(someList):
	for i in range(len(students)):
		print("first Nme - ",students[i]['first_name'],"Last name - ",students[i]['last_name'] )
iterateDictionary(students) 


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
	for i in range(len(some_list)):
		print(some_list[i][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
	for item,val in some_dict.items():
		print(len(val),item.upper())
		for v in range(len(val)):
			print(val[v])

printInfo(dojo)



















