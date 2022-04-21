class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(a):
            res = 0
            for i in range(len(a)):
                res += a[i] ** 2
            return res
        
        def split(n):
            return [int(x) for x in str(n)]
        dict = []
        while True:
            res = sq(split(n))
            n = res
            # print(res)
            if res in dict:
                return False
            if res == 1:
                return True
            dict.append(res)