# Find the element by index number
def findele(arr1, arr2):
    return [arr1[i] for i in arr2]

arr1 = [12,3,4,5,67, 90]
arr2 = [1, 0] #index number
print(findele(arr1, arr2))


# Method 2 (__getitem__)
def findele2(arr1, arr2):
    return list(map(arr1.__getitem__, arr2))

print(findele2(arr1, arr2))

