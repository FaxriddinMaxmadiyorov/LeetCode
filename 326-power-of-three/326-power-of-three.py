class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 100 % n == 0