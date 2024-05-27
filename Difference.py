arr1 = [10, 15, 20, 25, 30, 35, 40]
arr2 = [25, 40, 35]

temp = []
for i in arr1:
    if i not in arr2:
        temp.append(i)

print(temp)

