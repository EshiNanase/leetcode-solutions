class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        answer = []
        answer.append(max_sum)
        for i in range(1, len(nums)):
            answer.append(max(answer[i-1] + nums[i], nums[i]))
            if answer[i] > max_sum:
                max_sum = answer[i]
        return max_sum
        