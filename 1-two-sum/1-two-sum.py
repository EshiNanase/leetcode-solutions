class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for num_ind, num in enumerate(nums):
            difference = target - num
            needed_number = hashmap.get(difference)
            if needed_number is not None:
                return [needed_number, num_ind]
            hashmap[num] = num_ind
        return []