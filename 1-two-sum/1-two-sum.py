class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums[::-1])):
            for y in range(len(nums[::-1])):
                if x == y:
                    pass
                elif nums[x] + nums[y] == target:
                    return [x, y]
