class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return nums
        
        values = []
        stack = str(nums[0])
        prev = nums[0]
        for num_ind, num in enumerate(nums):
            if num - prev > 1:
                if int(stack) == prev:
                    values.append(stack)
                    stack = str(num)
                else:
                    stack += f'->{prev}'
                    values.append(stack)
                    stack = str(num)
            prev = num
        if int(stack) != prev:
            stack += f'->{prev}'
        values.append(stack)
        return values