class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            digit_a = a[i] if i < len(a) else 0
            digit_b = b[i] if i < len(b) else 0

            total = int(digit_a) + int(digit_b) + carry
            char_to_add = str(total % 2)
            res = char_to_add + res
            carry = total // 2

        if carry:
            res = str(carry) + res

        return res
