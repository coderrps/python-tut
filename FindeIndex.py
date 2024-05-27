arr1 = [1,2,3,4,5,7,1,4]
num = 1
res = []
for i in range(0, len(arr1)):
    if arr1[i] == num:
        res.append(i)

print(res)