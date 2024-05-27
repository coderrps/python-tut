def splitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        
        arr[n-1] = x


arr = [1,2,3,4,5,6,7,8,9]
n = len(arr) 
k = 2 

splitArray(arr, n, k)

for i in range(0, n):
    print(arr[i], end=' ')



print("\n")
def splitArr2(arr, n, k):
    b = arr[:k]
    return (arr[k::]+b[::])

arr2 = splitArr2(arr, n, k)
for i in range(0, n):
    print(arr2[i], end=' ')

