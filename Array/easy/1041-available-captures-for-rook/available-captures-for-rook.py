class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x0, y0 = i, j
                    break

        count = 0
        for dx, dy in dirs:
            x, y = x0 + dx, y0 + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "p":
                    count += 1
                    break
                if board[x][y] == "B":
                    break
                x += dx
                y += dy
        return count
