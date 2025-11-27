class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            elif stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                return False
        return len(stack) == 0