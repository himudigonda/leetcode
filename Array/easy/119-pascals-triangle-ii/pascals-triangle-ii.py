class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        res = 1
        ans.append(res)
        for col in range(1, rowIndex + 1):
            res = res * ((rowIndex) + 1 - col)
            res = res // col
            ans.append(res)
        return ans
