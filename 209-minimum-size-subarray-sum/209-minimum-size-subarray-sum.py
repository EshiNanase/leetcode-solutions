class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0     
        
        result = len(nums)
        result_calc = 0
        j = 0
        
        for i in range(len(nums)):
            
            result_calc += nums[i]
            
            while result_calc >= target:
                result_calc -= nums[j]
                result = min(result, i - j + 1)
                j += 1
        
        return result