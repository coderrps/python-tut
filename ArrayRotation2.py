def reverseArray_rotation(arr, d):
    c = (arr[d:]) + (arr[:d])
    return c 

arr = [1,2,3,4,5,6,7]
print(reverseArray_rotation(arr, 6))

def reverseArray2(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end] 
        arr[end] = temp
        start += 1 
        end -= 1 

def leftRotate(arr, d):
    n = len(arr)
    reverseArray2(arr, 0, d-1)
    reverseArray2(arr, d, n-1)
    reverseArray2(arr, 0, n-1)

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

leftRotate(arr, 2)
printArray(arr)