class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        s = list(s)
        stack = list()
        result = 0
        
        for symbol in s:
            if symbol not in stack:
                stack.append(symbol)
            else:
                result = max(result, len(stack))
                stack = stack[stack.index(symbol)+1:]
                stack.append(symbol)
        
        return max(result, len(stack))