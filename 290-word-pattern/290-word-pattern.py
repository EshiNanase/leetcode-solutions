class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_ = s.split()
        
        if len(pattern) != len(s_):
            return False
        
        hashmap = {}
        for letter, word in zip(pattern, s_):
            if letter not in hashmap and word not in hashmap.values():
                hashmap[letter] = word
            else:
                if hashmap.get(letter) != word:
                    return False
        return True