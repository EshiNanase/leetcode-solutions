class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        
        while i < j:
                
            min_val = min(height[i], height[j])
            result = max(result, min_val*(j - i))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
            
        return result