# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        values = []
        
        def recursion(root):
            
            if root.left:
                recursion(root.left)
            values.append(root.val)
            if root.right:
                recursion(root.right)
        
        recursion(root)
        
        diff = abs(values[1] - values[0])
        for i in range(1,len(values)):
            diff = min(diff, abs(values[i]-values[i-1]))
            
        return diff