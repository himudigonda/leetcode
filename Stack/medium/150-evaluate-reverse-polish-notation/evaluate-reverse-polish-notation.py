class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "*":
                    stack.append(a * b)
                elif token == "-":
                    stack.append(b - a)
                elif token == "+":
                    stack.append(b + a)
                else:
                    stack.append(int(b / a))
        return stack[0]
