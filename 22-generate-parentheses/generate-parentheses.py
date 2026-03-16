class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(cur, openn, closee):
            if openn == n and closee == n:
                res.append("".join(cur))
                return
            if openn < n:
                cur.append("(")
                generate(cur, openn + 1, closee)
                cur.pop()
            if closee < openn:
                cur.append(")")
                generate(cur, openn, closee + 1)
                cur.pop()

        generate([], 0, 0)
        return res
