class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for roman in range(len(s)):
            try:
                if dict[s[roman]] < dict[s[roman + 1]]:
                    answer += dict[s[roman + 1]] - dict[s[roman]] - dict[s[roman + 1]]
                else:    
                    answer += dict[s[roman]]
                print(answer)
            except IndexError:
                answer += dict[s[roman]]
                break
        
        return answer