class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for k in range(0, numRows):
            temp = []
            for i in range(0, k + 1):
                temp.append(self.fact(k) // (self.fact(i) * self.fact(k - i)))
                # print(k, i)
            res.append(temp)
        return res
    
    def fact(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res