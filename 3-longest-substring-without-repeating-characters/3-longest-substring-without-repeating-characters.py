class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == ' ':
            return 1
        
        substring = ''
        best = 0
        for i in s:
            substring += i
            while len(substring) != len(set(substring)):
                if best < len(substring[:-1]):
                    best = len(substring[:-1])
                substring = substring[1:]
                
        if best < len(substring):
            best = len(substring)

                
        return best if best != 0 else len(substring)