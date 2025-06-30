class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        res = 0
        r = n - 1

        p2 = [1] * n
        for i in range(1, n):
            p2[i] = (p2[i - 1] * 2) % mod

        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                # res += 2 ** (r - i)
                res = (res + p2[r - i]) % mod

        return res % mod
