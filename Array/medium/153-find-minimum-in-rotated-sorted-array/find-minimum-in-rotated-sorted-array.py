class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # best = nums[0]

        # while left <= right:
        #     mid = (left + right) // 2
        #     best = min(best, nums[mid])
        #     if nums[mid] < nums[right] and nums[mid] >= nums[left]:
        #         right = mid - 1
        #     elif nums[mid] > nums[right] and nums[mid] >= nums[left]:
        #         left = mid + 1
        #     elif nums[mid] < nums[right] and nums[mid] <= nums[left]:
        #         right = mid - 1
        #     else:
        #         print(nums[left], nums[right], nums[mid], left, right, mid)
        #         best = min(best, nums[mid], nums[left], nums[right])
        #         return best
        # return best

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]