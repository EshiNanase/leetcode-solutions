class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        for index in range(1, len(s)+1):
            substring = s[:index]
            for substring_index in range(len(substring)+1):
                substring1 = substring[substring_index:]
                if substring1 == substring1[::-1]:
                    palindromes.append(substring1)
        return max(palindromes, key=lambda x: len(x))