class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        n = n & (n - 1)
        return n == 0