class Node:
    # initializing the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # initialize next as null


class LinkedList:
    # initialize the head
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    # Starts with empty list
    llist = LinkedList()

    llist.head = Node(4)
    second = Node(9) 
    third = Node(0)
    fourth = Node(10)

    # Link the first node with the second
    llist.head.next = second
    # Link the second node with the third
    second.next = third 
    third.next = fourth

    llist.printList() 




