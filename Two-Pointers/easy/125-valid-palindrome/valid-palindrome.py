class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # BruteForce
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() == s[r].lower():
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True

        # Optimal
        # Clean up and then 2 points
        s = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
