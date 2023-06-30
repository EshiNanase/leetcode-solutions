class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substrings = [s[:ind] for ind, val in enumerate(s, start=1)]
        for substring in substrings:
            difference = len(s) // len(substring)
            if len(s) != len(substring) and substring * difference == s:
                return True
        return False
        