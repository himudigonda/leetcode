class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        counts = Counter(s)
        oddcounts = 0

        for count in counts.values():
            if count % 2 != 0:
                oddcounts = 1
                result += count - 1

            else:
                result += count
        return result + oddcounts
