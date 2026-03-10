class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posptr = 0
        negptr = 1
        res = [0] * len(nums)

        for n in nums:
            if n > 0:
                res[posptr] = n
                posptr += 2
            else:
                res[negptr] = n
                negptr += 2
        return res
