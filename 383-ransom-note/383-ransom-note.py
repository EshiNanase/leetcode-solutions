class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            if letter in magazine:
                magazine.pop(magazine.index(letter))
            else:
                return False
        return True
        