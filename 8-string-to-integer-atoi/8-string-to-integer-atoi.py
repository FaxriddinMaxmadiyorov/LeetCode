class Solution:
    def myAtoi(self, s: str) -> int:
        low, up = -2 ** 31, 2 ** 31 -1
        res = 0
        CountNumber, sign, Negative = False, False, False
        for i in range(len(s)):
            if sign == False and CountNumber == False and s[i] == ' ':
                continue
            elif CountNumber == False and sign == False and (s[i] == '+' or s[i] == '-'):
                sign = True
                if s[i] == '-':
                    Negative = True
            elif s[i] >= '0' and s[i] <= '9':
                res = res * 10 + int(s[i])
                CountNumber = True
                if Negative == True and -1 * res < low:
                    return low
                elif Negative == False and res > up:
                    return up
            else:
                break
        if Negative:
            return -1 * res
        return res