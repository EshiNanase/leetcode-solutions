class Solution:
    def arrangeCoins(self, n: int) -> int:
        row_length = 0
        rows = 0
        while n - row_length > 0:
            rows += 1
            row_length += 1
            n -= row_length
        return rows