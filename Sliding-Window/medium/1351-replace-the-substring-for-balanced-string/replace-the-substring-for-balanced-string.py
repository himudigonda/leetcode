class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        exp = n / 4
        freq = Counter(s)

        if all(freq[c] == exp for c in "QWER"):
            return 0

        left = 0
        res = n

        for right in range(n):
            freq[s[right]] -= 1

            while left < n and all(freq[c] <= exp for c in "QWER"):
                res = min(res, right - left + 1)
                freq[s[left]] += 1
                left += 1
        return res
