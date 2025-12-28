class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def isPalindrome(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(cur[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1)
                    cur.pop()

        backtrack(0)
        return res
