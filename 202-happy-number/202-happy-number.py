class Solution:
    def isHappy(self, n: int) -> bool:
        answer = n
        for i in range(10):
            numbers = [int(i) for i in str(answer)]
            answer = 0
            for i in numbers:
                answer += i**2
        if answer == 1:
            return True
        return False