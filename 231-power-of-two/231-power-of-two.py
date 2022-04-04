class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and n == 2 ** int(math.log(n, 2)):
            return True
        else:
            return False