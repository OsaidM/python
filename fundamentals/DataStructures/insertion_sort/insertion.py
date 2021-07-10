def insertion_sort(arr):
    for index in range(1,len(arr)):
        value = arr[index]
        i = index -1
        while i >= 0:
            if value < arr[i]: # assuming ascending order
                arr[i+1] = arr[i]
                arr[i] = value
                i -= 1
            else:
                break
    return arr
print(insertion_sort([7,6,5,3,4,1]))
