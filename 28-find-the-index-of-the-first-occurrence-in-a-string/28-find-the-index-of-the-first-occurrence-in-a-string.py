class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            answer = haystack.index(needle)
        except ValueError:
            return -1
        return answer
        