class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n % 2 == 0:
                n //= 2
            elif n == 1:
                return True
            else:
                return False
        