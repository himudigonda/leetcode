class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxstackLen = 0

        for ch in s:
            if ch == "(":
                stack.append("(")
                maxstackLen = max(maxstackLen, len(stack))

            elif ch == ")":
                stack.pop()
        return maxstackLen
