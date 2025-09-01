class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                stack.append(int(token))
            else:
                if token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
        return stack[0]
