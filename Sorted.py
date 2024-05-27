def sorting(arr1):
    arr2 = sorted(arr1, key=len)
    return arr2

arr1 = ["rohan", "amy", "sapna", "muhammad", 
       "akash", "raunak", "chinmoy"]
print(sorting(arr1))

sortedList = sorted(arr1, key=lambda x: len(x))
print(sortedList)