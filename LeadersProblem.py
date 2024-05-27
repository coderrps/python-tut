def leaders(a, n):
    lead = []
    maxi = a[-1]
    lead.append(maxi)

    for i in range(n-2, -1, -1):
        if a[i] >= maxi:
            lead.append(a[i])
            maxi = a[i]

    lead.reverse()
    return lead


n = 6
A = [16, 17, 4, 3, 5, 2]
print(leaders(A, n))  

n = 5
A = [1, 2, 3, 4, 0]
print(leaders(A, n)) 