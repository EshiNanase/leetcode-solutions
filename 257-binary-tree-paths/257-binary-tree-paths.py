# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        answer = []
        
        def traversal(tree, path):
            path = f'{path}{tree.val}'
            if tree.left:
                traversal(tree.left, f'{path}->')
            if tree.right:
                traversal(tree.right, f'{path}->')
            if not tree.left and not tree.right:
                answer.append(path)
        traversal(root, '')
        return answer