class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            bits = []
            while i:
                diff = i % 2
                bits.append(diff)
                i //= 2
            result.append(bits.count(1))
        return result