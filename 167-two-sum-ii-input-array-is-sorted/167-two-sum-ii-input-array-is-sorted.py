class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            pseudo_target = numbers[i] + numbers[j]
            if pseudo_target == target:
                return [i+1, j+1]
            else:
                if pseudo_target < target:
                    i += 1
                else:
                    j -= 1 # если больше, то спускаемся, меньше - поднимаемся