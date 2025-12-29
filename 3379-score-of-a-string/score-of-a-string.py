class Solution:
    def scoreOfString(self, s: str) -> int:
        asciis = []
        for ch in s:
            asciis.append(ord(ch))

        res = []
        for i in range(1, len(asciis)):
            res.append(abs(asciis[i] - asciis[i - 1]))
        return sum(res)
