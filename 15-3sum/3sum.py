class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for anchor in range(len(nums) - 2):
            if anchor > 0 and nums[anchor] == nums[anchor - 1]: continue

            left = anchor + 1
            right = len(nums) - 1
            
            while left < right:
                cur = nums[anchor] + nums[left] + nums[right]
            
                if cur == 0:
                    res.append([nums[anchor], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    right -= 1
        return res