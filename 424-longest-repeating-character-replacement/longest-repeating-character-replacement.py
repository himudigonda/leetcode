class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        maxlen = 0
        curlen = 0
        mapping = defaultdict(int)

        for right in range(len(s)):
            mapping[s[right]] += 1
            curlen += 1
            maxfreq = max(mapping.values())
            if curlen - maxfreq > k:
                mapping[s[left]] -= 1
                curlen -= 1
                left += 1
            maxlen = max(curlen, maxlen)
        # return len(s) - left
        return maxlen
