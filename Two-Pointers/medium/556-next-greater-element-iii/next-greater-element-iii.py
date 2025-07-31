class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2

        # Find the first digit that is smaller than its next digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # If no such digit is found, return -1
        if i == -1:
            return -1

        # Find the smallest digit on the right side of i that is bigger than digits[i]
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Swap them
        digits[i], digits[j] = digits[j], digits[i]

        # Reverse the subarray to the right of i
        digits[i + 1 :] = reversed(digits[i + 1 :])

        result = int("".join(digits))
        return result if result < (1 << 31) else -1
