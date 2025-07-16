class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vow = 0
        cons = 0
        vset = "aeiouAEIOU"
        for ch in word:
            if ch.isalpha():
                if ch in vset:
                    vow += 1
                else:
                    cons += 1
            elif not ch.isdigit():
                return False
        return vow >= 1 and cons >= 1
