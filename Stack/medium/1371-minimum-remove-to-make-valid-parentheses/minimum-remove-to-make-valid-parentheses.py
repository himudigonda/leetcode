class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = list(s)
        for ptr in range(len(s)):
            ch = s[ptr]
            if ch == "(":
                stack.append(ptr)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    res[ptr] = ""
        if stack:
            for idx in stack:
                res[idx] = ""
        return "".join(res)
