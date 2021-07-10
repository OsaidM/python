def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]: # assuming ascending order
                arr[i], arr[j] = arr[j], arr[i]
        
    return arr
print(selection_sort([7,6,5,3,4,1]))
