impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut dp = vec! [0; m];
        let mut res = 0;

        for i in 0..n{
            let mut prev = 0;
            for j in 0..m{
                dp[j] += grid[i][j];
                prev += dp[j];
                if prev <= k{
                    res += 1
                }
            }
        }
        return res
    }
}