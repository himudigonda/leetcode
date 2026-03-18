class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mapping = defaultdict(int)
        maxsum = -1

        for num in nums:
            digit = max(str(num))

            if digit in mapping:
                maxsum = max(maxsum, mapping[digit] + num)
            mapping[digit] = max(mapping[digit], num)
        return maxsum
