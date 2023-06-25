class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        vowels_exist = []
        consonants_exist = ''
        for smth in s:
            if smth in vowels:
                vowels_exist.append(smth)
                consonants_exist += '_'
            else:
                consonants_exist += smth
        
        for vowel in reversed(vowels_exist):
            consonants_exist = consonants_exist.replace('_', vowel, 1)
        
        return consonants_exist