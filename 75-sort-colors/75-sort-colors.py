class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = True
        while swapped:
            swapped = False
            for ind, num in enumerate(nums[:-1]):
                if nums[ind] > nums[ind+1]:
                    nums[ind], nums[ind+1] = nums[ind+1], nums[ind]
                    swapped = True