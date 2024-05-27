# Native Method
def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if(arr[i] > max): 
            max = arr[i]
    return max 


if __name__ =="__main__":
    arr = [1, 3, 5, 78, 56, 91]
    n = len(arr)
    print("Largest is:" , largest(arr, n))

# Max function
def largest_max(arr2, n2):
    ans = max(arr2)  
    return ans 

if __name__ == "__main__":
    arr2 = [1, 3, 5, 78, 56, 23]
    n2 = len(arr2)
    print(largest_max(arr2, n2))

# Sort Function
def large_sort(arr3, n3):
    arr3.sort()  

    return arr3[n3-1]

arr3 = [42, 45, 89, 83, 67]
n3 = len(arr3) 
print(large_sort(arr3, n3))

# Lambda Function
array = [23, 45, 78, 91, 23]
largest_ele = max(array, key=lambda x: x) 
print(largest_ele)