class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(current_str, open_count, closed_count):
            if open_count == n and closed_count == n:
                result.append(current_str)
                return
            if open_count < n:
                backtracking(current_str + "(", open_count + 1, closed_count)
            if closed_count < open_count:
                backtracking(current_str + ")", open_count, closed_count + 1)

        backtracking("", 0, 0)
        return result
