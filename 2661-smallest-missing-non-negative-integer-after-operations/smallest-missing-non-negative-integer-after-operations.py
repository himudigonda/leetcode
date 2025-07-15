class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value
        for num in nums:
            freq[num % value] += 1
        
        # mex = 0
        # while True:
        #     if freq[mex % value] > 0:
        #         freq[mex % value] -= 1
        #         mex += 1
        #     else:
        #         break
        # return mex

        mincount = min(freq)
        for i, count in enumerate(freq):
            if count == mincount:
                return mincount * value + i