class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            temp = []
            if i == 1:
                temp.append(1)
            elif i == 2:
                temp.append(1)
                temp.append(1)
            else:
                temp.append(1)
                for j in range(1, i - 1):
                    temp.append(res[i - 2][j - 1] + res[i - 2][j])
                temp.append(1)
            res.append(temp)
        return res