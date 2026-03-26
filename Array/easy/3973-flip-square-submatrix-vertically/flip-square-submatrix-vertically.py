class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        top = x
        bottom = x + k - 1
        left = y
        right = y + k - 1

        while top < bottom:
            grid[top][left : right + 1], grid[bottom][left : right + 1] = (
                grid[bottom][left : right + 1],
                grid[top][left : right + 1],
            )
            top += 1
            bottom -= 1
        return grid
