class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = list(Counter(deck).values())

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        res = vals[0]
        for i in range(1, len(vals)):
            res = gcd(res, vals[i])
            if res < 2:
                return False
        return res >= 2
