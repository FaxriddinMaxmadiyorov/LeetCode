class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        if n > 0:
            for i in bin(n):
                if i == '1':
                    cnt += 1
            return cnt == 1
        else:
            return False