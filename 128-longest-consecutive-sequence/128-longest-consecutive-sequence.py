class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        
        values = []
        stack = [nums[0]]
        for num in nums[1:]:
            
            if stack[-1] + 1 == num:
                stack.append(num)
            else:
                values.append(len(stack))
                stack = [num]
        
        values.append(len(stack))
        return max(values)