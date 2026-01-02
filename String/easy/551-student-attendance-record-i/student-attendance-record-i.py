class Solution:
    def checkRecord(self, s: str) -> bool:
        lllcount = 0
        acount = 0

        for day in s:
            if day == "A":
                lllcount = 0
                acount += 1
                if acount == 2:
                    return False
            elif day == "L":
                lllcount += 1
                if lllcount == 3:
                    return False
            else:
                lllcount = 0
        return True
