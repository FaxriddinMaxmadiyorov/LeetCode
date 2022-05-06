class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(t)):
            if i < len(s) and s[i] == t[i]:
                continue
            else:
                return t[i]