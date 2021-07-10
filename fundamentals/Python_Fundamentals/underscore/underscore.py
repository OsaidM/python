class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                return iterable[i]
        
    def filter(self, iterable, callback):
        iterable2 = [] 
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                iterable2.append(iterable[i])
            
        return iterable2
    def reject(self, iterable, callback):
        iterable2 = [] 
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                iterable2.append(iterable[i])
        return iterable2
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable #that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)# should return [2, 4, 6] after you finish implementing the code #above
square = _.map([1, 2, 3,4], lambda x: x*2) 
find = _.find([1, 2, 3, 4, 5, 6], lambda x: x>4)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 != 0)

print(evens)
print(find)
print(square)
print(odds)

                
