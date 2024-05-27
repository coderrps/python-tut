def Union(arr1, arr2):
    result = arr1 + arr2 
    return sorted(result)

arr1 = [23, 15, 2, 14, 14, 16, 20 ,52]
arr2 = [2, 48, 15, 12, 26, 32, 47, 54]

print(Union(arr1, arr2))
