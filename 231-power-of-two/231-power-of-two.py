class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        two = 1
        while two <= n:
            if two == n:
                return True
            two *= 2
        return False