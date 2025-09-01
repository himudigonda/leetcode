class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # BFS Optimal with visited()
        # islands = 0
        # visited = set()
        # ROWS = len(grid)
        # COLS = len(grid[0])

        # def bfs(r, c):
        #     q = deque()
        #     visited.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (
        #                 0 <= r < ROWS
        #                 and 0 <= c < COLS
        #                 and grid[r][c] == "1"
        #                 and (r, c) not in visited
        #             ):
        #                 q.append((r, c))
        #                 visited.add((r, c))

        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "1" and (row, col) not in visited:
        #             islands += 1
        #             bfs(row, col)
        # return islands

        if not grid:
            return

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):

            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "-1"
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                dfs(r, c)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
