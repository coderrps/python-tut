from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postorder(root, target):
            if root is None: 
                return None

            root.left = postorder(root.left, target)
            root.right = postorder(root.right, target)

            if root.left is None and root.right is None and root.val == target:
                return None
            return root

        return postorder(root, target)

# Helper function to build a tree from a list
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

# Helper function to print the tree (inorder traversal)
def print_tree(root: Optional[TreeNode]):
    if root is None:
        return
    print_tree(root.left)
    print(root.val, end=' ')
    print_tree(root.right)

# Function to take user input and build the tree
def input_tree() -> List[Optional[int]]:
    values = input("Enter the tree values in level order: ").split()
    return [int(val) if val != 'null' else None for val in values]

# Main function
def main():
    # Taking input from the user
    values = input_tree()
    target = int(input("Enter the target value to remove: "))
    
    root = build_tree(values)
    
    print("Original tree (inorder):")
    print_tree(root)
    print()
    
    solution = Solution()
    root = solution.removeLeafNodes(root, target)
    
    print("Tree after removing target leaves (inorder):")
    print_tree(root)
    print()

if __name__ == "__main__":
    main()
