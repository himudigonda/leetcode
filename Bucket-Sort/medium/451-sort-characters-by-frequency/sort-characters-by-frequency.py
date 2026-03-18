class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
        res = ""
        for key, val in sorted_counts:
            res += key * val
        return res
