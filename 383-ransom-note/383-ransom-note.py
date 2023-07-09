class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        usable_letters = {key:magazine.count(key) for key in set(magazine)}
        for letter in ransomNote:
            counted_letter = usable_letters.get(letter)
            if counted_letter:
                usable_letters[letter] -= 1
            else:
                return False
        return True