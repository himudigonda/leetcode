class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        ROWS = len(grid)
        COLS = len(grid[0])
        num_islands = 0

        def dropIsland(row, col):
            if (
                row >= ROWS
                or col >= COLS
                or row < 0
                or col < 0
                or grid[row][col] != "1"
            ):
                return
            grid[row][col] = "-1"
            dirs = [
                [0,1],
                [0,-1],
                [1,0],
                [-1,0]
            ]
            for i, j in dirs:
                dropIsland(row + i, col + j)
            return
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    num_islands += 1
                    dropIsland(i, j)
        return num_islands
