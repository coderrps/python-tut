# Kadane's Algorithm
# hello
def maxSubArray(arr, N):
    count = 0
    maxi = float('-inf')
    for i in range(N):
        count += arr[i]
        maxi = max(maxi, count)
        if count<0:
            count = 0
    return maxi


if __name__ == '__main__':
    arr = [1,2,3,-2,5]
    N = len(arr)  
    print(maxSubArray(arr, N))
    