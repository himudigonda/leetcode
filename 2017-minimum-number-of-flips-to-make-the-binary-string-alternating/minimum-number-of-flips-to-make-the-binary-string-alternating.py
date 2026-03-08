class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s * 2

        # target1 = ""
        # target2 = ""

        # for i in range(len(s)):
        #     target1 += "0" if i % 2 == 0 else "1"
        #     target2 += "1" if i % 2 == 0 else "0"

        diff1, diff2 = 0, 0
        minFlips = float("inf")
        left = 0

        for right in range(len(s)):
            # if s[right] != target1[right]:
            #     diff1 += 1
            # if s[right] != target2[right]:
            #     diff2 += 1
            if int(s[right]) != (right % 2):
                diff1 += 1
            if int(s[right]) != (1 - (right % 2)):
                diff2 += 1

            if (right - left + 1) > n:
                # if s[left] != target1[left]:
                #     diff1 -= 1
                # if s[left] != target2[left]:
                #     diff2 -= 1
                # left += 1
                if int(s[left]) != (left % 2):
                    diff1 -= 1
                if int(s[left]) != (1 - (left % 2)):
                    diff2 -= 1
                left += 1

            if (right - left + 1) == n:
                minFlips = min(minFlips, diff1, diff2)

        return minFlips
