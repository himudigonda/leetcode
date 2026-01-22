class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        original_color = image[sr][sc]
        if original_color == color:
            return image

        ROWS = len(image)
        COLS = len(image[0])

        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            if image[r][c] == original_color:
                image[r][c] = color
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        q.append((nr, nc))
        return image
