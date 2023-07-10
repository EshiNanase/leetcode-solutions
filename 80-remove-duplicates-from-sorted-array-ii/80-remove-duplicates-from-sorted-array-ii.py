class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique_nums = list(set(nums))
        
        for num in range(len(unique_nums)):
            number = unique_nums[num]
            counted_num = nums.count(number)
            for _ in range(max(0, counted_num - 2)):
                nums.remove(number)
        return len(nums)