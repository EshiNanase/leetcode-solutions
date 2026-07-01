class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_value = int(a, 2) + int(b, 2)
        result = ""
        while int_value:
            diff_value = int_value // 2
            result += str(int_value % 2)
            int_value = diff_value
        return result[::-1] or "0"