class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split(' ')):
            return False
        
        if pattern == s:
            return True
        
        patterns = {key:value for key, value in zip(pattern, s.split(' '))}
        if len(list(set(list(patterns.values())))) != len(list(patterns.values())):
            return False
        return True if ' '.join([patterns[i] for i in pattern]) == s else False