class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        
        count = 0
        for i in zeros:
            nums.pop(i-count)
            count += 1
            nums.append(0)