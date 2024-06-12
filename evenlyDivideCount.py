class Solution:
    def evenlyDivides(self, N):
        count = 0
        n = N 
        while(n != 0):
            a = n % 10
            n = n // 10
            if (a == 0):
                continue
            if (N% a ==0):
                count += 1
        return count
    
try:
    N = int(input())
    sol = Solution()
    print("The count is:", sol.evenlyDivides(N))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")