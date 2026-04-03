class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        posidx, negidx = 0, 1

        for i in nums:
            if i < 0:
                ans[negidx] = i
                negidx += 2
            else:
                ans[posidx] = i
                posidx += 2
        return ans
