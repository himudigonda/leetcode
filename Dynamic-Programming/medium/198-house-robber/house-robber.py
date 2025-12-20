class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for pointer in nums:
            temp = max(pointer + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
