class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        s = s.strip()
        if not s:
            return 0
        if s[0] == "-":
            neg = -1
            s = s[1:]
        elif s[0] == "+":
            neg = 1
            s = s[1:]
        
        else:
            neg = 1

        def rec(idx):
            if idx >= len(s):
                return
            if s[idx].isdigit():
                res.append(s[idx])
            else:
                # if res: return
                return
            rec(idx + 1)

        rec(0)
        INT_MIN = -(2**31)  # -2147483648
        INT_MAX = 2**31 - 1  # 2147483647
        res = int("".join(res)) if res else 0
        res = max(INT_MIN, min(INT_MAX, neg * res))
        return res
