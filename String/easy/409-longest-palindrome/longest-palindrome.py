class Solution:
    def longestPalindrome(self, s: str) -> int:
        # odd_count = 0
        # mapping = defaultdict(int)

        # for ch in s:
        #     mapping[ch] += 1
        #     if mapping[ch] % 2 == 1:
        #         odd_count += 1
        #     else:
        #         odd_count -= 1
        # if odd_count > 0:
        #     return len(s) - odd_count + 1
        # return len(s)

        mapping = defaultdict(int)
        res = 0
        for ch in s:
            mapping[ch] += 1
        oddlen = False

        for freq in mapping.values():
            if not freq % 2:
                res += freq
            else:
                res += freq - 1
                oddlen = True
        if oddlen:
            res += 1
        return res
