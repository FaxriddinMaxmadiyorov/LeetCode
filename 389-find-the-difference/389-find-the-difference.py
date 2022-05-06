class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = s + t
        v = 0
        for i in s:
            v = v ^ ord(i)
        return chr(v)
    # 0 ^ a = a ^ 0 = a
    # a ^ b ^ c = c ^ a ^ b