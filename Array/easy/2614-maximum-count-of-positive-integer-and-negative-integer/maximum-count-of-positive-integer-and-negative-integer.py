import bisect


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # # BruteForce
        # positive_count = 0
        # negative_count = 0
        # for num in nums:
        #     if num > 0:
        #         positive_count += 1
        #     elif num < 0:
        #         negative_count += 1
        # return max(positive_count, negative_count)

        # # Optimal (inbuilt bisect)
        # negative_count = bisect.bisect_left(nums, 0)
        # first_positive_idx = bisect.bisect_left(nums, 1)
        # positive_count = len(nums) - first_positive_idx
        # return max(negative_count, positive_count)

        # Optimal (No inbuilt)
        def lower_bound(target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        negative_count = lower_bound(0)
        first_positive_idx = lower_bound(1)
        positive_count = len(nums) - first_positive_idx
        return max(negative_count, positive_count)
