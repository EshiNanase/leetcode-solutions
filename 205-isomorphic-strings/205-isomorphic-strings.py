class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s = list(s)
        t = list(t)
        
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for first_letter, second_letter in zip(s, t):
            letter = hashmap.get(first_letter)
            if not letter and second_letter not in hashmap.values():
                hashmap[first_letter] = second_letter
            else:
                if letter != second_letter:
                    return False
        return True