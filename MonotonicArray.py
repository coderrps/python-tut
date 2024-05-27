def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True 
    return False 

# A = [3,2,1,2,3] # False
A = [5,6,7,8,8] # True
print(isMonotonic(A))