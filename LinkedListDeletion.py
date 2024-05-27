# Three types of deletion: Beginning, Middle, End

class TreeNode:
    def __init__(self, data):
        self.number = data
        self.next = None 

def push(head, A):
    n = TreeNode(A)
    n.number = A
    n.next = head 
    head = n
    return head


# Deleting the Node
def deleteN(head, position):
    temp = head
    prev = head 
    for i in range(0, position):
        if i == 0 and position == 1:
            head = head.next 
        else:
            if i == position-1 and temp is not None:
                prev.next = temp.next 
            else:
                prev = temp

                if prev is None:
                    break
                temp = temp.next
    return head 


def printList(head):
    while(head):
        if head.next == None:
            print("[", head.number, "] ", "[", hex(id(head)), "]->", "nil")
        else:
            print("[", head.number, "] ", "[", hex(
                id(head)), "]->", hex(id(head.next)))
        head = head.next
    print("")
    print("")

head = TreeNode(0)
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)

printList(head)

head = deleteN(head, 1)
printList(head)