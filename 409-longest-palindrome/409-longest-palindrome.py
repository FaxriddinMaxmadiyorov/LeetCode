class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res, odd = 0, False
        for i in d:
            if d[i] % 2 == 0:
                res += d[i]
            else:
                res += d[i] - 1
                odd = True
        if odd:
            res += 1
        return res