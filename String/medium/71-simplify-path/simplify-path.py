class Solution:
    def simplifyPath(self, path: str) -> str:
        # # BruteForce
        # stack = []
        # cur = ""
        # for c in path + "/":
        #     if c == "/":
        #         if cur == "..":
        #             if stack:
        #                 stack.pop()
        #         elif cur != "" and cur != ".":
        #             stack.append(cur)
        #         cur = ""
        #     else:
        #         cur += c
        # return "/" + "/".join(stack)

        # Optimal
        stack = []
        for token in path.split("/"):
            if token == "..":
                if stack:
                    stack.pop()
            elif token and token != ".":
                stack.append(token)
        return "/" + "/".join(stack)
