class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value
        for num in nums:
            remainder = num % value
            freq[remainder] += 1
        mex = 0
        while True:
            target_remainder = mex % value
            if freq[target_remainder] > 0:
                freq[target_remainder] -= 1
                mex += 1
            else:
                break
        return mex