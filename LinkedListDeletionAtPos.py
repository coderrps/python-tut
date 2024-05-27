# Delete a Linked List node at a given position

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return
        index = 0 
        current = self.head 
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1 
        if index < position:
            print("\nIndex out of range")
        elif index == 0:
            self.head = self.head.next 
        else:
            previous.next = current.next 

    
    def printList(self):
        temp = self.head 
        while(temp):
            print(" %d " % (temp.data), end = " ")
            temp = temp.next 


llist = LinkedList()
llist.push(7)
llist.push(1) 
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()
llist.deleteNodeAtGivenPosition(1)
print("\nLinked List after Deletion at position 1: ")
llist.printList()



""""
def deleteList(self):
    current = self.head
    while current:
        next_to_current = current.next
        del current
        current = next_to_current

"""