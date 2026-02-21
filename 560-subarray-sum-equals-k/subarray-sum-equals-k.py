class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0: 1}
        cursum = 0
        count = 0

        for num in nums:
            cursum += num
            diff = cursum - k

            count += mapping.get(diff, 0)
            mapping[cursum] = mapping.get(cursum, 0) + 1
        return count
