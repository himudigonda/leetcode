class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # # Binary Search
        # count = 0
        # n = len(grid[0])

        # for row in grid:
        #     left, right = 0, n - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if row[mid] < 0:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     count += n - left
        # return count

        # StairCase Method
        m = len(grid)
        n = len(grid[0])
        count = 0
        row_idx = m - 1
        col_idx = 0

        while row_idx >= 0 and col_idx < n:
            if grid[row_idx][col_idx] < 0:
                count += n - col_idx
                row_idx -= 1
            else:
                col_idx += 1
        return count
