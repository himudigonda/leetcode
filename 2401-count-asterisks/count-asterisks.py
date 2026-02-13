class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = True

        counts = 0
        for ch in s:
            if ch == "|":
                flag = not flag
            if flag:
                if ch == "*":
                    counts += 1
        return counts
