def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    
    return x * power(x, y // 2) * power(x, y // 2)

def order(x):
    n=0
    while (x != 0):
        n = n + 1
        x = x // 10

    return  n  

def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while(temp  != 0):
        r = temp % 10 
        sum1 = sum1 + power(r, n)
        temp = temp // 10 

    return (sum1 == x)

x = 153 
print(isArmstrong(x))

x = 1253
print(isArmstrong(x))


print("\n")
print("Second Method")

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    if sum == num:
        return True
    else :
        return False
    
num = 153
print(is_armstrong(num))


print("\n")
print("Third Method Ternary Operator")

def is_armstrong3(num3):
    return sum(int(digit)**len(str(num3)) for digit in str(num3)) == num3 

num3 = 1253 
if is_armstrong3(num3):
    print("Yes")
else:
    print("No")