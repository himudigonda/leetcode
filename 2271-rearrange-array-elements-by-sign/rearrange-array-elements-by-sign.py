class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0 for _ in range(length)]
        posidx, negidx = 0, 1

        for i in range(length):
            if nums[i] < 0:
                ans[negidx] = nums[i]
                negidx += 2
            else:
                ans[posidx] = nums[i]
                posidx += 2
        return ans
