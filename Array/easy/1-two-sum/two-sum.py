class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # BruteForce
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimal
        mapping = defaultdict(int)
        for idx, val in enumerate(nums):
            if target - val in mapping:
                return [idx, mapping[target - val]]
            mapping[val] = idx
