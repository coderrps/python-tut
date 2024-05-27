# Inserting at the beginning
def push(self, new_data):

    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node


# Inserting at specific position 
def insertAfter(self, prev_node, new_data):

    if prev_node is None:
        return
    
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

# Inserting at the end of the linked list 
def insertlast(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
        self.head = new_node
        return 
    
    last = self.head 
    while(last.next):
        last = last.next 

    last.next = new_node 
    