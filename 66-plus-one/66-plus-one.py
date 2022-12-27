class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        start = str(int(''.join(digits)) + 1)
        middle = [int(i) for i in start]
        return middle