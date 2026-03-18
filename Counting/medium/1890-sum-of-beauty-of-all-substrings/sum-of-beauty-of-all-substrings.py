class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        # left = 0
        # right = 0
        for left in range(len(s)):
            counts = defaultdict(int)

            for right in range(left, len(s)):
                counts[s[right]] += 1
                vals = counts.values()
                maax = max(vals)
                miin = min(vals)
                res += maax - miin

            # counts[s[right]] += 1
            # maax = max(counts.values())
            # miin = min(counts.values())
            # res += maax - miin
        return res
