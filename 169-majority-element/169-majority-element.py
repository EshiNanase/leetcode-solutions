class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 0
        while num == 0:
            if str(nums).count(str(max(nums))) > len(nums)/2:
                num = max(nums)
            else:
                nums.pop(nums.index(max(nums)))
        return num