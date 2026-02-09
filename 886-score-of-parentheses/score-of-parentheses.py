class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack = [0]

        # for ch in s:
        #     if ch == "(":
        #         stack.append(0)
        #     else:
        #         num = stack.pop()
        #         score = max(2 * num, 1)
        #         stack[-1] += score
        # return stack[0]

        ans = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == "(":
                    ans += 2**depth
        return ans
