class Solution:
    def simplifyPath(self, path: str) -> str:
        # # Iter 1
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

        # Iter 2
        stack = []
        for token in path.split("/"):
            if token == "..":
                if stack:
                    stack.pop()
            elif token and token != ".":
                stack.append(token)
        return "/" + "/".join(stack)
        # arr = [i for i in path.split('/')]
        # for i in arr:
        #     if i == '..':
        #         stack.pop()
        #     elif i == ".":
        #         continue
        #     else:
        #         stack.append(i)
