class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        oranges = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    oranges += 1
        if oranges == 0:
            return 0
        if not q:
            return -1

        time = 0
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while q and oranges > 0:
            # qlen = len(q)
            # for qidx in range(qlen):
            #     i, j, t = q.popleft()
            #     for dr, dc in dirs:
            #         ni, nj = i + dr, j + dc
            #         if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == 1:
            #             grid[ni][nj] = 2
            #             oranges -= 1
            #             q.append((ni, nj))
            # time += 1
            i, j, t = q.popleft()
            for dr, dc in dirs:
                ni, nj = i + dr, j + dc
                if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    time = t + 1
                    q.append((ni, nj, time))
                    oranges -= 1
        # time += 1
        return time if oranges == 0 else -1
