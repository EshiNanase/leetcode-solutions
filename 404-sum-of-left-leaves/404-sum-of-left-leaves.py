# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        values = []
        
        def traversal(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    values.append(root.left.val)
                traversal(root.left)
            if root.right:
                traversal(root.right)
                
        traversal(root)
        return sum(values)