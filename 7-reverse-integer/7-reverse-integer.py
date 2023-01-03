import string

class Solution:
    def reverse(self, x: int) -> int:
        number = list(str(x)[::-1])
        if number[-1] in string.punctuation:
            punc = number[-1]
            number.pop(-1)
            
            answer = int(punc + ''.join(number))
            
            if -2**31 < answer < (2**31)-1:
                return answer
            else:
                return 0
        else:
            answer = int(''.join(number))
            if -2**31 < answer < (2**31)-1:
                return answer
            else:
                return 0