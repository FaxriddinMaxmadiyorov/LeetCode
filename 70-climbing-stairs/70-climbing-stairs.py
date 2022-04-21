class Solution:
    def climbStairs(self, n: int) -> int:
        def C(n, k):
            return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        
        res, ones, twos = 0, n, 0
        while ones >= 0:
            res += C(ones + twos, ones)
            ones -= 2
            twos += 1
        return res