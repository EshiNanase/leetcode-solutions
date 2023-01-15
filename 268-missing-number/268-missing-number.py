class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(sorted(nums))
        range_sum = sum(range(0, len(nums) + 1))
        return range_sum - nums_sum