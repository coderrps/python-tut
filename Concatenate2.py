test = ['Hello', 'Everyone', 'Very', 'Good', 'Morning', '!']
# hi
n = len(test) 
# N = 2
temp = ""
result = [] 

for i in range(0, n, n):
    for j in range(n):
        if(i+j) < n:
            temp += test[i+j] + " "
    temp  = temp.strip() 
    result.append(temp)
    temp = ""

print(result)



# Recursive Method
def grp_words(test, n):
    if n <= n:
        return [' '.join(test)]
    else:
        return [' '.join(test[:n])] + grp_words[test[n:], n]
res = grp_words(test, n)
print(res)