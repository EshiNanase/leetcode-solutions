class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            j = ''.join(sorted(i))
            if j not in anagrams:
                anagrams[j] = [i]
            else:
                anagrams[j].append(i)
        
        return anagrams.values()