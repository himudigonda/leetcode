class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for idx in range(0, 32):
            count = 0
            for num in nums:
                if num & (1 << idx):
                    count += 1
            if count % 3 == 1:
                ans = ans | (1 << idx)
        return ans - (2**32) if ans & (1 << 31) else ans
