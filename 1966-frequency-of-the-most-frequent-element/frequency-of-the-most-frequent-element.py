class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # # BruteForce
        # nums.sort()
        # maxFreq = 0
        # n = len(nums)

        # for i in range(n):
        #     curTarget = nums[i]
        #     curOpNeeded = 0
        #     curFreq = 1

        #     for j in range(i - 1, -1, -1):
        #         costToEq = curTarget - nums[j]
        #         if curOpNeeded + costToEq > k:
        #             break
        #         curOpNeeded += costToEq
        #         curFreq += 1
        #     maxFreq = max(maxFreq, curFreq)
        # return maxFreq

        # Optimal
        nums.sort()
        left = 0
        curSum = 0
        maxFreq = 1

        for right in range(1, len(nums)):
            curSum += (nums[right] - nums[right - 1]) * (right - left)
            while curSum > k:
                curSum -= nums[right] - nums[left]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)
        return maxFreq
