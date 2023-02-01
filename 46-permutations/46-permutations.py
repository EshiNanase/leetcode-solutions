class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:\
        
        answer = []
        
        if len(nums) == 1:
            return [nums]
        
        if len(nums) == 2:
            for q in nums:
                for w in nums:
                    answer.append([q, w])
        
        if len(nums) == 3:
            for q in nums:
                for w in nums:
                    for e in nums:
                        answer.append([q, w, e])
        
        if len(nums) == 4:
            for q in nums:
                for w in nums:
                    for e in nums:
                        for r in nums:
                            answer.append([q, w, e, r])
        
        if len(nums) == 5:
            for q in nums:
                for w in nums:
                    for e in nums:
                        for r in nums:
                            for t in nums:
                                answer.append([q, w, e, r, t])
        
        if len(nums) == 6:
            for q in nums:
                for w in nums:
                    for e in nums:
                        for r in nums:
                            for t in nums:
                                for y in nums:
                                    answer.append([q, w, e, r, t, y])
        
        count = 0
        while count < len(answer):
            for i in answer[count]:
                if answer[count].count(i) > 1:
                    answer.pop(count)
                    count -= 1
                    break
            count += 1  
        return answer
                
                        
        