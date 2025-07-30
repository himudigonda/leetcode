class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = 0
        for num in nums:
            maxor |= num

        count = 0

        def backtrack(index, curor):
            nonlocal count

            if index == len(nums):
                if curor == maxor:
                    count += 1
                return

            backtrack(index + 1, curor | nums[index])
            backtrack(index + 1, curor)

        backtrack(0, 0)
        return count
