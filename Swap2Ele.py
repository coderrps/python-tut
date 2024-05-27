def swap2(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list 

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3 
print(swap2(List, pos1-1, pos2-1))

def swap22(list, pos1, pos2):
    first_ele = list.pop(pos1)   
    second_ele = list.pop(pos2-1)
    
    list.insert(pos1, second_ele)  
    list.insert(pos2, first_ele)  
     
    return list

List2 = [23, 65, 19, 90]
pos11, pos22  = 1, 3
 
print(swap22(List2, pos11-1, pos22-1))



def swap222(list, pos1, pos2):
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get  

    return list 
List3 = [23, 65, 19, 90]
 
pos111, pos222  = 1, 3
print(swap222(List3, pos111-1, pos222-1))



def swap4(list, pos1, pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp 
    return list 

