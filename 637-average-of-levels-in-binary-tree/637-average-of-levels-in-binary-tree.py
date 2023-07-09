# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hashmap = defaultdict(list)
        def recursion(root, level):
            if root.left:
                recursion(root.left, level+1)
            if root.right:
                recursion(root.right, level+1)
            hashmap[level].append(root.val)
        recursion(root, 0)
        values = []
        for level in sorted(list(hashmap.keys())):
            level_values = hashmap[level]
            values.append(sum(level_values)/len(level_values))
        return values