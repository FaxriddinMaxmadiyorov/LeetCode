class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            res.append([1] * i)
            if i > 2:
                for j in range(1, i - 1):
                    res[i - 1][j] = res[i - 2][j - 1] + res[i - 2][j]
        return res