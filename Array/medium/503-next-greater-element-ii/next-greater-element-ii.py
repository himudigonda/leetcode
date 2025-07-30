class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        stack = []
        d = {}
        i = 0
        n = len(nums)
        while i < 2 * n:
            cur = nums[i % n]
            while stack and cur > nums[stack[-1]]:
                d[stack.pop()] = cur
            if i < n:
                stack.append(i)
            i += 1
        for i in stack:
            d[i] = -1
        return [d[i] for i in range(n)]
