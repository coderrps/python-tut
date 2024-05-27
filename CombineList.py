arr1 = [1, 5, 6, 9, 11]
arr2 = [3, 4, 7, 8, 10]

size1 = len(arr1)  
size2 = len(arr2)

res = [] 
i, j = 0, 0

while i < size1 and j < size2:
    if arr1[i] < arr2[j]:
        res.append(arr1[i])
        i += 1 
    else:
        res.append(arr2[j])
        j += 1 

res = res + arr1[i:] + arr2[j:]   
print(res)

# Method 2
result = sorted(arr1 + arr2) 
print(result)