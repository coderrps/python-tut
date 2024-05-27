arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

for i in arr2:
    arr1.append(i)
print(arr1)


# Second Method
array1 = [1,2,3]
array2 = ['a', 'b', 'c']
def merge(array1, array2):
    if not array1:
        return array2
    if not array2:
        return array1
    return [array1[0], array2[0]] + merge(array1[1:], array2[1:])
print(merge(array1, array2))

# Third Method
merged = []
min_len = min(len(array1), len(array2))

for i in range(min_len):
    merged.append(array1[i])
    merged.append(array2[i])

merged += array1[min_len:] + array2[min_len:]
print(merged)