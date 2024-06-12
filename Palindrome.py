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
    

    def palindrom(n):
        if n == ans:
            return True
        else: 
            return False
        

n = int(input())
ans = Solution.reverse_int(n)
print("Palindrome is:", Solution.palindrom(n))

