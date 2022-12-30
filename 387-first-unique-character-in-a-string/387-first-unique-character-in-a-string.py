class Solution:
    def firstUniqChar(self, s: str) -> int:
        repetable = {i:0 for i in list(s)}
        for letter in s:
            repetable[letter] += 1
            
        for letter in s:
            if repetable[letter] == 1:
                return list(s).index(letter)
        return -1