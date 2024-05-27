print("Factorial Function in python")
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)

num = 5
print(factorial(num))

print("\n")
print("Using math library")
import math 
def factorial2(n):
    return (math.factorial(n))

num2 = 4 
print(factorial2(num2))