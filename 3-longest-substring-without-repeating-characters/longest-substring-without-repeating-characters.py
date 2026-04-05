class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curlen = 0
        maxlen = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                curlen -= 1
            seen.add(s[right])
            curlen += 1
            maxlen = max(curlen, maxlen)
        return maxlen
