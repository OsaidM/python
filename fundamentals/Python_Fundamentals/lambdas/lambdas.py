'''
def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list

print( map([1,2,3,4], (lambda num: num * num) ))
print( map([1,2,3,4], (lambda num: num * 3) ))
print( map([1,2,3,4], (lambda num: num / num) ))
print( map([1,2,3,4], (lambda num: num % 2) ))



def invoker(callback):
    print(callback(2))
    
invoker(lambda x: 2*x)

'''


my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a #lambda as the first argument
