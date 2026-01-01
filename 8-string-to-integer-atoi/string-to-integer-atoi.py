class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        direction = 1
        res = 0
        chidx = 0

        if s[0] == "+":
            chidx += 1
        elif s[0] == "-":
            chidx += 1
            direction = -1

        while chidx < len(s) and s[chidx].isdigit():
            res = res * 10 + int(s[chidx])
            chidx += 1
        res = res * direction

        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if res < MIN_INT:
            return MIN_INT
        if res > MAX_INT:
            return MAX_INT
        return res
