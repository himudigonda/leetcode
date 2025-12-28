class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current_arr, brackets_open, brackets_close):
            # if len(current_arr) == n * 2:
            if brackets_open == n and brackets_close == n:
                res.append("".join(current_arr))
                return
            if brackets_open < n:
                current_arr.append("(")
                dfs(current_arr, brackets_open + 1, brackets_close)
                current_arr.pop()
                # dfs(current_arr, brackets_open, brackets_close)
                # return
            if brackets_close < brackets_open:
                current_arr.append(")")
                dfs(current_arr, brackets_open, brackets_close + 1)
                current_arr.pop()
                # dfs(current_arr, brackets_open, brackets_close)
                # return

        dfs([], 0, 0)
        return res
