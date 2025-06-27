class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        expfreq = n / 4

        # m = defaultdict(int)
        # for letter in s:
        #     m[letter] += 1
        m = Counter(s)

        if max(m.values()) == expfreq:
            return 0

        left = 0
        ans = float("inf")

        for right in range(n):
            m[s[right]] -= 1

            while left <= right and max(m.values()) <= expfreq:
                ans = min(ans, right - left + 1)
                m[s[left]] += 1
                left += 1
        return ans
