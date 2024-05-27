def aSum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

# Main Function
if __name__ == "__main__":
    arr = [1,2,3,45,6]

    n = len(arr)
    ans = aSum(arr)
    print("Sum of the array is:", ans)


# Use Built-In Function - sum()

print("\n")
print("Second Method- Use Built-In Function sum()")

arr2 = [12,34,342,90]
ans2 = sum(arr2)
print(ans2)

print("\n")
print("Third Method- Reduce Method")

from functools import reduce
def sum3(arr3):
    sum = reduce(lambda a, b: a+b, arr3)
    return (sum)
arr3 = []
arr3 = [1,2,3,4]
n = len(arr3)
ans3 = sum3(arr3)
print(ans3)



print("\n")
print("Fourth Method- Divide and Conquer")

def sum_of_array(arr4, low, high):
    if low == high:
        return arr4[low]
    mid = (low+high) // 2
    left_sum = sum_of_array(arr4, low, mid)
    right_sum = sum_of_array(arr4, mid+1, high)
    return left_sum+right_sum

arr4 = [15,45,23,90,38]
print(sum_of_array(arr4, 0, len(arr4)- 1))