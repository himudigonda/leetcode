class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        numss = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                numss.append(nums[i])

        res = 0
        for cur in range(1, len(numss) - 1):
            if (
                numss[cur - 1] < numss[cur] > numss[cur + 1]
                or numss[cur - 1] > numss[cur] < numss[cur + 1]
            ):
                res += 1
        return res
