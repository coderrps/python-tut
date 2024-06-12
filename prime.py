series = list(map(int, input().split()))

def isPrime(num):
    i = 2
    while i*i <= num:
        if num%i==0:
            return False
        i += 1
    return True

k = 20 
primes = [1]*(k+1)
primes[0] = primes[1] = 0

for i in range(2, k+1):
    if isPrime(i):
        primes[i] = 1
    else:
        primes[i] = 0

print(primes)



# for item in series:
#     ans = isPrime(item)
#     print(item, ans)
