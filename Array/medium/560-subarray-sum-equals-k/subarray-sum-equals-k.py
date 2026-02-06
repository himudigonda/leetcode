class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if k == 1: return 1
        # if len(nums) == 1: return 0
        # left = 0
        # prefix = [0]
        # for idx, val in enumerate(nums):
        #     prefix.append(prefix[-1] + val)
        # count = 0
        # for right in range(1, len(prefix)):
        #     if prefix[right] - prefix[left] <= k:
        #         count += 1
        #     else:
        #         left += 1
        # return count

        mapping = {0: 1}
        cursum = 0
        count = 0

        for num in nums:
            cursum += num
            diff = cursum - k
            # if diff in mapping:
            count += mapping.get(diff, 0)
            mapping[cursum] = mapping.get(cursum, 0) + 1
        return count