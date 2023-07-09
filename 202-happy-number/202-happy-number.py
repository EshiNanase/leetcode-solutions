class Solution:
    def isHappy(self, n: int) -> bool:
        sys.set_int_max_str_digits(9999999)
        count = 0
        while n != 1 and count < 30:
            digits = list(str(n))
            for digit_ind, digit in enumerate(digits):
                digits[digit_ind] = int(digit)**2
            n = sum(digits)
            count += 1
        
        if count == 30:
            return False
        
        return True