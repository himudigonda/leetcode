class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sol = 0
        ops = ['-', '+', '/', '*']
        for token in tokens:
            if token in ops:

                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(b / a)
            else:
                stack.append(token)
        return int(stack[0])