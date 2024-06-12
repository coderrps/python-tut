class Maths:
    def addition(a, b):
        addRes = a+b
        return addRes
    
    def sub(a, b):
        subRes = a-b
        return subRes
    
    def mul(a, b):
        mulRes = a*b
        return mulRes
    
    def div(a, b):
        return a/b
    
    def pow(a, b):
        return a**b
    
    def mod(a, b):
        return a % b
    
    def factorial(n):
        if n < 0:
            return "Error"
        elif n == 0 or n == 1:
            return 1
        else:
            fact = 1
            for i in range(2, n+1):
                fact *= i
            return fact 
        
    def gcd(a, b):
        while b:
            a, b = b, a% b
        return a
    
    def lcm(a, b):
        return abs(a * b) // Maths.gcd(a, b)

try:
    a = int(input())
    b = int(input())
    
    print("Addition: ", Maths.addition(a, b))
    print("Subtraction: ", Maths.sub(a, b))
    print("Multiplication: ", Maths.mul(a, b))
    print("Division: ", Maths.div(a, b))
    print("Power: ", Maths.pow(a, b))
    print("Modulus: ", Maths.mod(a, b))
    print("Factorial: ", Maths.factorial(n=5))
    print("GCD: ", Maths.gcd(a, b))
    print("LCM: ", Maths.lcm(a, b))

except ValueError:
    print("Invalid input. Please enter valid integers.")