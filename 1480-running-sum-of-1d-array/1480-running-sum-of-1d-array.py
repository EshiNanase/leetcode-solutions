class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        summed = 0
        for i in nums:
            summed += i
            answer.append(summed)
        return answer