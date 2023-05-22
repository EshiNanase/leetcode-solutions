# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        maxies = []
        def traversal(tree, curr_sum):
            
            curr_sum += tree.val
            if not tree.left and not tree.right:
                maxies.append(curr_sum)
            if tree.left:
                traversal(tree.left, curr_sum)
            if tree.right:
                traversal(tree.right, curr_sum)
        
        if root:
            traversal(root, 0)
        else:
            return False
        
        return True if targetSum in maxies else False