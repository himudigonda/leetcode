class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        carry = 1
        while carry and ptr >= 0:
            summ = carry + digits[ptr]
            carry = summ // 10
            digits[ptr] = summ % 10
            ptr -= 1
        if carry:
            digits = digits[::-1]
            digits.append(carry)
            digits = digits[::-1]
        return digits
