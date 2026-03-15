class Solution:
    def countCommas(self, n: int) -> int:
        # blocks = math.floor(math.log(n, 10))
        blocks = len(str(n)) - 1
        
        if blocks < 3:
            return 0

        groups = blocks // 3
        res = 0
        for i in range(1, groups):
            res += (10 ** (3 * (i + 1)) - 10 ** (3 * i)) * i
        res += groups * (n - 10 ** (groups * 3) + 1)
        return res
