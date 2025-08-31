class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}": "{", ")": "(", "]": "["}

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack and len(stack) > 0 and i in mapping and stack[-1] == mapping[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False
