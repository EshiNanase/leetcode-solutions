# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def get_tree(tree):
            
            values = []
            
            def traversal(tree):
                
                if tree.left and tree.right:
                    traversal(tree.left)
                    traversal(tree.right)
                elif tree.left and not tree.right:
                    traversal(tree.left)
                elif tree.right and not tree.left:
                    traversal(tree.right)
                    values.append(None)
                    
                values.append(tree.val)
            
            traversal(tree)
            return values
        
        if p == q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        
        return True if p==q or get_tree(p) == get_tree(q) else False
        