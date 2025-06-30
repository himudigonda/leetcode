class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for anchor in range(len(nums) - 2):
            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            left = anchor + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[left] + nums[right] + nums[anchor]
                if summ == 0:
                    ans.append([nums[anchor], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        return ans
