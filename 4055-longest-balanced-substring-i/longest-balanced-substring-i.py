class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        s = [ord(ch) - ord('a') for ch in s]
        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxFreq = 0

            for j in range(i, n):
                if freq[s[j]] == 0:
                    distinct += 1
                freq[s[j]] += 1
                maxFreq = max(maxFreq, freq[s[j]])
                length = j - i + 1
                if length == distinct * maxFreq:
                    ans = max(ans, length)
        return ans