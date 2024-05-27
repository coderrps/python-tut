# Step1: TreeNode Class 
# Step2: build_tree function
# Step3: print_tree function
# step4: input_tree function
# step5: insert_leaf function
# step6: main function

from typing import Optional, List 

# TreeNode Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right


# build_tree Function --> Helper Function to build a tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None 
    
    root = TreeNode(values[0])
    queue = [root] 
    i = 1 
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# print_tree function 
def print_tree(root: Optional[TreeNode]):
    if root is None:
        return
    print_tree(root.left)
    print(root.val, end=' ')
    print_tree(root.right)

# print_tree function --> helper function to print inorder traversal tree
def input_tree() -> List[Optional[int]]:
    values = input("Enter the tree values: ").split()
    return [int(val) if val != 'null' else None for val in values]


# insert_leaf function --> func to insert leaf node
def insert_leaf(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(value)
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None:
            node.left = TreeNode(value)
            break 
        else:
            queue.append(node.left)
        
        if node.right is None:
            node.right = TreeNode(value)
            break
        else:
            queue.append(node.right)

    return root 


# main function
def main():
    value = input_tree()

    root = build_tree(value)

    print("Original tree: ")
    print_tree(root)
    print()

    new_leaf_value = int(input("Enter the new leaf node to insert: "))
    root = insert_leaf(root, new_leaf_value)

    print("Tree after inserting: ")
    print_tree(root)
    print() 

if __name__ == '__main__':
    main()