class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [self.combinations(rowIndex, i) for i in range(rowIndex + 1)]
    def combinations(self, n, m):
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))