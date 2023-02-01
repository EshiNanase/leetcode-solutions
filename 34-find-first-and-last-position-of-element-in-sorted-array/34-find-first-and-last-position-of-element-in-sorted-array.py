class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        count = 0
        for i in nums:
            if i == target and first == -1:
                first = count
                last = count
                count += 1
            
            elif i == target:
                last = count
                count += 1
            
            else:
                count += 1
                
        return [first, last]