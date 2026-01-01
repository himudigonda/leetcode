class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for j in range(len(digits) - 1, -1, -1):
            if j == len(digits) - 1:
                temp = digits[j] + carry + 1
            else:
                temp = digits[j] + carry
            carry = temp // 10
            digits[j] = temp % 10
        if carry:
            digits.insert(0, carry)
        return digits
