class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        three = 3
        for i in range(63):
            if n != three:
                three *= 3
            else:
                return True
        return False