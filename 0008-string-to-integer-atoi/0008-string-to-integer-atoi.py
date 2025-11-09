class Solution:
    def myAtoi(self, s):
        s = s.lstrip()  # Step 1: Remove leading whitespaces
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] in ['-', '+']:  # Step 2: Check sign
            sign = -1 if s[0] == '-' else 1
            i += 1

        num = 0
        # Step 3: Read digits until a non-digit is found
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # Step 4: Clamp the value to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
