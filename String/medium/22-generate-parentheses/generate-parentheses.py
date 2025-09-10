class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # With a string
        # result = []

        # def backtracking(current_str, open_count, closed_count):
        #     if open_count == n and closed_count == n:
        #         result.append(current_str)
        #         return
        #     if open_count < n:
        #         backtracking(current_str + "(", open_count + 1, closed_count)
        #     if closed_count < open_count:
        #         backtracking(current_str + ")", open_count, closed_count + 1)

        # backtracking("", 0, 0)
        # return result

        # With an array
        result = []
        string = []

        def backtracking(open_count, closed_count):
            if open_count == n and closed_count == n:
                result.append("".join(string))
                return
            if open_count < n:
                string.append("(")
                backtracking(open_count + 1, closed_count)
                string.pop()
            if closed_count < open_count:
                string.append(")")
                backtracking(open_count, closed_count + 1)
                string.pop()

        backtracking(0, 0)
        return result
