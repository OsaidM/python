
# 1
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = '30'

print(z)

# =============================================================
# 2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        student_dict = students[i]
        for k in student_dict:
            if k == 'first_name':
                newStr = k + ' - ' + student_dict[k]
        for key in student_dict:
            newStr2 =  key + ' - ' + student_dict[key]
        print(newStr + ', ' + newStr2)
        
iterateDictionary(students)
# =============================================================
# 3

def iterDict2(key_name, students):
	for i in range(len(students)):
		for key in students[i]:
			if key == key_name and key_name == 'first_name':
				print(students[i][key])
			elif key == key_name and key_name == 'last_name':	
				print(students[i][key])
iterDict2('last_name',students)
# =============================================================

# 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    
    for key in dojo:
        arr = dojo[key]
        print(len(arr), key)
        #print(arr)
        for i in range(len(arr)):
            print(arr[i])


printInfo(dojo)


