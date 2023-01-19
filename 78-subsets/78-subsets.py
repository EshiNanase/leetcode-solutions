class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def proccess(i,subset):
            if i>=len(nums):
                answer.append(subset)
                return
            proccess(i+1,subset+[nums[i]])
            proccess(i+1,subset)
        
        proccess(0,[])

        return answer        
       