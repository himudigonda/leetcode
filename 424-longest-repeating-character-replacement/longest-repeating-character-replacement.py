class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxfreq = 0
        mapping = defaultdict(int)
        # right = 0
        # maxlen = 0
        # curlen = 0

        for right in range(len(s)):
            mapping[s[right]] += 1
            # curlen += 1
            maxfreq = max(maxfreq, mapping[s[right]])
            # maxfreq = max(mapping.values())
            if (right - left + 1) - maxfreq > k:
                mapping[s[left]] -= 1
                # curlen -= 1
                left += 1
            # maxlen = max(right - left + 1, maxlen)
        return len(s) - left
        # return maxlen
