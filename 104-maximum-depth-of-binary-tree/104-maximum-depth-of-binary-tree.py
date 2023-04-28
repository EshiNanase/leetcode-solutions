# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        depths = []
        
        def get_depth(branch, curr_depth):
            if branch.left:
                get_depth(branch.left, curr_depth+1)
            if branch.right:
                get_depth(branch.right, curr_depth+1)
            else:
                depths.append(curr_depth)
        get_depth(root, 1)
        return max(depths)