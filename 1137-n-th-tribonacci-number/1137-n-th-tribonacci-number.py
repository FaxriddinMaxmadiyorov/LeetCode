class Solution:
    def tribonacci(self, n: int) -> int:
        f = []
        f.append(0)
        f.append(1)
        f.append(1)
        for i in range(3, n + 1):
            s = f[i-1]+f[i-2]+f[i-3]
            f.append(s)
        return f[n]