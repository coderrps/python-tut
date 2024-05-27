print("Swap Using tuple variable")
def swap(list):
    get = list[-1], list[0]

    list[0], list[-1] = get

    return list 

newList = [12, 34, 56, 22, 12, 10]
print(swap(newList))


print('\n')

print("Swap using * Operand")
def swapList2(list2):
    start, *middle, end = list2
    list2 = [end, *middle, start] 

    return list2 
newList = [12, 45, 78, 98, 34]
print(swapList2(newList))


print('\n')


print("Using POP Method")
def swapPop(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

newList = [12, 45, 35, 90, 45]
print(swapPop(newList))


print("\n")

print("Swap Using Slicing")
def swapSlice(list):
    if len(list) >= 2:
        list = list[-1:] + list[1:-1] + list[:1]

    return list 

inp = [34, 89, 70, 56, 33, 87]
print(swapSlice(inp))


print("\n")


print("Max Function")
def maxi(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


lst = [1, 2, 3, 6]
print(maxi(lst))