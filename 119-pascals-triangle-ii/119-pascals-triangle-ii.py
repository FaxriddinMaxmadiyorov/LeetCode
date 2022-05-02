class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [[0 for i in range(rowIndex + 1)] for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(i + 1):
                a[i][j] = 1
                
        for i in range(2, rowIndex + 1):
            for j in range(i + 1):
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        return a[i][:rowIndex + 1]