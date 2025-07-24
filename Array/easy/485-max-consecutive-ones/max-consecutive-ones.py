class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlength = 0
        length = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                length = 0
            maxlength = max(maxlength, length)
        return maxlength
