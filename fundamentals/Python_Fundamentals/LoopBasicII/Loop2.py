# 1
#def biggieSize(list):
#	for i in range(0,len(list),1):
#		if list[i] > 0:
#			list[i] = "big"
#	return list
#print(biggieSize([-1, 3, 5, -5]))

#2
#def countPositive(list):
#	sum = 0
#	lastI = len(list)
#	for i in range(0,len(list),1):
#		if list[i] > 0:
#			sum += 1
#	list[-1] = sum
#	return list
#print(countPositive([-1,1,1,1]))

#3
#def sumTotal(list):
#	sum = 0
#	for i in range(0,len(list),1):
#		sum += list[i]
#	return sum
#print(sumTotal([1,2,3,4]))

#4
#def average(list):
#	avg = 0
#	sum = 0
#	for i in range(0,len(list),1):
#		sum += list[i]
#	avg = sum / len(list)
#	return avg
#print(average([1,2,3,4]))


#5
#def length(list):
#	return len(list)
#
#print(length([37,2,1,-9]))

#6
#def min(list):
#	min = 0
#	for i in range(0,len(list),1):
#		if min < list[i]:
#			 continue
#		else:
#			min = list[i]
#	return min
#print(min([37,2,1,-9]))

#7
#def max(list):
#	max = 0
#	for i in range(0,len(list),1):
#		if max > list[i]:
#			continue
#		else:
#			max = list[i]
#	return max
#print(max([37,2,1,-9]))


#8
#def ultAnalys(list):
#	dict = {}
#	max = 0
#	sum = 0
#	min = 0
#	for i in range(0,len(list),1):
#		sum += list[i]
#		if max > list[i]:
#			max = max
#		else:
#			max = list[i]
#		
#		if min < list[i]:
#			min = min
#		else:
#			min = list[i]
#		
#	avg = sum / len(list)
#	dict.update({"sumTotal": sum, "average":avg, "minimum": min,"maximum":max,"length":len(list)})
#	return dict
#print(ultAnalys([37,2,1,-9]))

#9
def revList(list):
	return (list[::-1])

print(revList([37,2,1,-9]))
