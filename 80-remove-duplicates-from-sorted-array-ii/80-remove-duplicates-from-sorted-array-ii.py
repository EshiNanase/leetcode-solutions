class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        from copy import copy
        
        nums2 = copy(nums)
        
        for num in nums2:
            counted_num = nums.count(num)
            for _ in range(max(0, counted_num - 2)):
                nums.remove(num)
        return len(nums)