class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_listed = sorted(list(s))
        t_listed = sorted(list(t))
        
        if s_listed == t_listed:
            return True
        return False