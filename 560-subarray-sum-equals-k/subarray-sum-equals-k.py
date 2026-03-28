class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        mapping[0] = 1

        presum = 0
        count = 0

        for i in range(0, len(nums)):
            presum += nums[i]
            remove = presum - k
            count += mapping[remove]
            mapping[presum] += 1
        return count
