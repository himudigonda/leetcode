class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in mapp:
                stack.append(i)
            else:
                if not stack or stack[-1] != mapp[i]:
                    return False
                stack.pop()
        return len(stack) == 0
