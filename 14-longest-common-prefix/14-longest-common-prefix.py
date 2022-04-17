class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def f(s1, s2):
            res = ""
            n1 = len(s1)
            n2 = len(s2)
            i, j = 0, 0
            while i < n1 and j < n2:
                if s1[i] == s2[j]:
                    res += s1[i]
                else:
                    return res
                i += 1
                j += 1
            return res
        if len(strs) > 1:
            a = strs[0]
            for i in range(1, len(strs)):
                b = strs[i]
                a = f(a, b)
            return a
        else:
            return strs[0]