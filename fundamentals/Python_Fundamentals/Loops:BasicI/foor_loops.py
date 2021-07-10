#1.
#for i in range(150):
#	print(i)

#2.
#for i in range(5,1000, 5):
#	print(i)

#3.
#for i in range(1,100,1):
#	if i % 10 == 0:
#		print("Coding Dojo")
#	elif i % 5 == 0:
#		print("Coding")
#	print(i)

#4.
#sum =0
#for i in range(0,500000,1):
#	if i % 2 == 0:
#		sum += i
#print(sum)	

#5.
#for i in range(2018,0,-4):
#	print(i)


#6.
lowNum=2
highNum=9
mult = 3

for lowNum in range(lowNum,highNum+1,1):
	if lowNum % mult == 0:
		print(lowNum)
