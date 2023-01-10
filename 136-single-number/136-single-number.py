from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        doubles = {1: [], 2:[]}
        
        for i in set(nums):
            if nums.count(i) > 1:
                doubles[2].append(i)
            else:
                doubles[1].append(i)
        
        return doubles[1][0]
        