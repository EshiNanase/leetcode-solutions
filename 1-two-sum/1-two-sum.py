class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for num_ind, num in enumerate(nums):
            for existing_num in hashmap:
                if existing_num + num == target:
                    return sorted([hashmap[existing_num], num_ind])
            hashmap[num] = num_ind
        return []