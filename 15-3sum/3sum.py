class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for anchor in range(n - 2):
            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            if nums[anchor] > 0:
                break
            left = anchor + 1
            right = n - 1
            while left < right:
                total = nums[anchor] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[anchor], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
