class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 0 and n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False