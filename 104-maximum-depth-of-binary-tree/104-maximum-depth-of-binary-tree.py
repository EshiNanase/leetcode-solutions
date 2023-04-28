# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(branch, curr_depth):
            if not branch:
                return curr_depth
            else:
                return max(get_depth(branch.left, curr_depth+1), get_depth(branch.right, curr_depth+1))
        
        return get_depth(root, 0)