class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        if not digits:
            return 0
        ans = 0
        counts = Counter(digits)

        for i in range(100, 1000, 2):
            hundreds = i // 100
            tens = (i // 10) % 10
            ones = i % 10
            store = counts.copy()
            valid = True
            for d in [hundreds, tens, ones]:
                if store[d] == 0:
                    valid = False
                    break
                store[d] -= 1
            if valid:
                ans += 1
        return ans
