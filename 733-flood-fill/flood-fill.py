class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        targetcolor = image[sr][sc]
        if targetcolor == color:
            return image

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(i, j):
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or image[i][j] != targetcolor:
                return
            image[i][j] = color
            dirs = [
                [1, 0],
                [0, 1],
                [0, -1],
                [-1, 0],
            ]

            for dr, dc in dirs:
                dfs(i + dr, j + dc)
            return

        dfs(sr, sc)
        return image
