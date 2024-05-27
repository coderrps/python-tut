from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postorder(root, target):
            if root == None: return None 

            root.left = postorder(root.left, target)
            root.right = postorder(root.right, target)

            if root.left == root.right and root.val == target:
                return None 
            return root
        return postorder(root, target)



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

# Main function
def main():
    # Example usage
    values = [1, 2, 3, 2, None, 2, 4]
    target = 2
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


