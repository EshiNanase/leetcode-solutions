class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        values = []
        nums = list(set(nums))
        try:
            for i in range(3):
                max_number = max(nums)
                nums.remove(max_number)
                values.append(max_number)
        except ValueError:
            return max(values)
        return max_number