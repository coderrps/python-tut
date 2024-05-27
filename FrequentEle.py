def mostFreq(arr):
    count = 0
    num = arr[0]

    for i in arr:
        curr_freq = arr.count(i)
        if(curr_freq > count):
            count = curr_freq
            num = i
    return num 

arr = [1,2,2,2,3,45,6,3,2]
print(mostFreq(arr))

def mostFreq2(arr):
    return max(set(arr), key = arr.count)

print(mostFreq2(arr))