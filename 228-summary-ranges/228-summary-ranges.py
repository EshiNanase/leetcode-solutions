class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        stack = []
        for j, i in enumerate(nums):
            stack.append(i)
            if j+1 < len(nums) and nums[j] + 1 == nums[j+1]:
                pass
            else:
                if len(stack) == 1:
                    answer.append(str(stack[0]))
                else:
                    answer.append(f'{min(stack)}->{max(stack)}')
                stack = []
        
        return answer