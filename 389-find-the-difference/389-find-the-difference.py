class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return ''.join(list(set([i for i in t if s.count(i) != t.count(i)])))