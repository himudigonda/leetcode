func countSubmatrices(grid [][]int, k int) int {
	ROWs := len(grid)
	COLS := len(grid[0])
	dp := make([]int, COLS)
	res := 0

	for i := 0; i < ROWs; i++ {
		prev := 0
		for j := 0; j < COLS; j++ {
			dp[j] += grid[i][j]
			prev += dp[j]
			if prev <= k {
				res++
			} else {
				break
			}
		}
	}
	return res
}