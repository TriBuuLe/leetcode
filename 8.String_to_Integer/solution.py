class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 1. Skip whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check overflow BEFORE adding
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result