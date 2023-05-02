class Solution:
    def search(self, nums: List[int], target: int) -> int:
        initial = [i for i in range(max(nums) + 1)]
        if target in initial:
            if target in nums:
                return nums.index(target)
        return -1