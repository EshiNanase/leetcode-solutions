class Solution:
    def reverseBits(self, n: int) -> int:
        int_value = n
        result = ["0" for _ in range(32)]
        count = -1
        while int_value:
            diff_value = int_value // 2
            result[count] = str(int_value % 2)
            int_value = diff_value
            count -= 1
        
        result = "".join(result[::-1]) or "0"

        int_result = 0
        for ind, bit in enumerate(result[::-1]):
            int_result += int(bit) * 2 ** ind
        return int_result