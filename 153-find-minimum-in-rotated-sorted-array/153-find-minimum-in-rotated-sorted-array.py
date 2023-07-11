class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_length = len(nums)
        i = 0
        first_num = nums[0]
        
        while i < nums_length-1:
            i += 1
            if nums[i] < first_num:
                return nums[i]
            
        return first_num