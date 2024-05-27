def swapList(newList):
    size = len(newList)


    # First Method
    # temp = newList[0]
    # newList[0] = newList[size - 1]
    # newList[size - 1] = temp


    # Second Method
    newList[0], newList[-1] = newList[-1], newList[0] 

    return newList

newList = [12, 35, 9, 23, 78, 90]

print(swapList(newList))