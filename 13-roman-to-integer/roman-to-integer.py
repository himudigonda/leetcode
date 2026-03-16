class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = 0
        total = 0

        for char in s[::-1]:
            val = mapping[char]
            if val >= prev:
                total += val
            else:
                total -= val
            prev = val
        return total
