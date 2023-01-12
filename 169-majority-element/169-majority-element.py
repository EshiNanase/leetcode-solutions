class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max([num for num in set(nums) if str(nums).count(str(num)) > len(nums)/2])