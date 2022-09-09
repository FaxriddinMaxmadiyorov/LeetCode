class Solution:
    def convertToBase7(self, num: int) -> str:
        temp, res = abs(num), ""
        while temp >= 0:
            res += str(temp % 7)
            temp //= 7
            if temp == 0:
                break
        res = "".join(reversed(res))
        if num < 0:
            return "-" + res
        return res