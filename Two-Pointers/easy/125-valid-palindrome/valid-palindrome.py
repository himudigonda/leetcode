import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # 2 pointer approach using smart pointer movement
        # s = s.lower()
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # regex method
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        return cleaned == cleaned[::-1]