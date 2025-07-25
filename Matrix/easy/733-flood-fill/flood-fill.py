class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        oldcolor = image[sr][sc]
        if oldcolor == color:
            return image

        def dfs(r, c):
            dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            if (
                r < 0
                or c < 0
                or r >= len(image)
                or c >= len(image[0])
                or image[r][c] != oldcolor
            ):
                return
            image[r][c] = color

            for nr, nc in dirs:
                nr = r + nr
                nc = c + nc
                dfs(nr, nc)

        dfs(sr, sc)
        return image
