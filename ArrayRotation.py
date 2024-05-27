def reverse(start, end, arr):
    n_reverse = end - start + 1 
    count = 0 
    while((n_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count += 1
    return arr 

def left_rotate(arr, size, d):
    start = 0
    end = size - 1
    arr = reverse(start, end, arr)

    start = 0
    end = size - d - 1
    arr = reverse(start, end, arr)

    start = size - d
    end = size - 1 
    arr = reverse(start, end, arr)
    return arr 

arr = [1,2,3,4,5,6,7,8]
size = 8 
d = 3

if(d <= size):
    print(left_rotate(arr, size, d))
else:
    d = d % size 
    print(left_rotate(arr, size, d))



# Second Method
def rotateArray(arr2, n2, d2):
    temp = []
    i = 0
    while (i<d2):
        temp.append(arr2[i])
        i = i + 1
    i = 0
    while(d2<n2):
        arr2[i] = arr2[d2] 
        i = i + 1 
        d2 = d2 + 1 
    arr2[:] = arr2[: i] + temp 
    return arr2

arr2 = [1, 2, 3, 4, 5, 6, 7]
print(rotateArray(arr2, len(arr2), 2))