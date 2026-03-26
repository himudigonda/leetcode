class Solution:
    def generateRow(self, row: int) -> int:
        ans = 1
        ansRow = []
        ansRow.append(1)
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            res.append(self.generateRow(i + 1))
        return res
