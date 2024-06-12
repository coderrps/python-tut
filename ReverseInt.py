class Solution:
    def reverse_int(n):
        reversed_n = 0
        negative = n < 0
        n = abs(n)   

        while n != 0:
            digit = n%10 
            reversed_n = reversed_n * 10 + digit
            n = n // 10

        if negative:
            reversed_n = - reversed_n
        return reversed_n
    
n = int(input())

print("Reversed Integer: ", Solution.reverse_int(n))

