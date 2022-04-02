class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        k = 0
        while True:
            x = int(9 * math.pow(10, k) * (1 + k))
            if n > x:
                n -= x
                k += 1
            else:
                k += 1
                break
            print(n, k)
        if n % k == 0:
            num = int(math.pow(10, k-1)) + n // k - 1
            return num % 10
        else:
            num = int(math.pow(10, k-1)) + n // k
            return (num // int(math.pow(10, k-(n%k)))) % 10