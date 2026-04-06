class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorofall = 0
        for i in range(len(nums)):
            xorofall = xorofall ^ nums[i]

        rightmost = (xorofall & (xorofall - 1)) ^ xorofall

        b1 = 0
        b2 = 0

        for i in range(len(nums)):
            if nums[i] & rightmost:
                b2 = b2 ^ nums[i]
            else:
                b1 = b1 ^ nums[i]
        return [b1, b2]
