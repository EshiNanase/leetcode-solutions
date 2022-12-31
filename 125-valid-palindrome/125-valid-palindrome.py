import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for strin in string.punctuation:
            s = s.replace(strin, '')
        s = s.lower()
        
        if len(s) == 1 or len(s) == 0:
            return True
        
        s = s.replace(' ', '')
        
        count = 0
        for i in range(int(len(s)/2)):
            if s[i] == s[::-1][i]:
                count += 1
                if count == int(len(s)/2):
                    return True
            else:
                return False