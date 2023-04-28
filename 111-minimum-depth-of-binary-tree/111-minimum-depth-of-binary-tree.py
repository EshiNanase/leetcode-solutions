# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        depths = []
        
        if not root:
            return 0
        
        def recursion(branch, depth):
            if not branch.left and not branch.right:
                depths.append(depth)
            else:
                if branch.left:
                    recursion(branch.left, depth+1)
                if branch.right:
                    recursion(branch.right, depth+1)
                
        recursion(root, 1)
        return min(depths)
        