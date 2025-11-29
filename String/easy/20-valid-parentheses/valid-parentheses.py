class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != mapping[ch]:
                        return False
        return len(stack) == 0