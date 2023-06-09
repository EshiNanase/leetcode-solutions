class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        import string
        target_index = string.ascii_lowercase.find(target)
        lexicographically_greater = string.ascii_lowercase[target_index:]
        values = {letter:lexicographically_greater.find(letter) for letter in letters if letter != target and letter in lexicographically_greater}
        return min(values, key=values.get) if values else letters[0]