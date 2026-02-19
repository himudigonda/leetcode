class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        nums = nums
        for num in nums:
            if stack:
                while stack and stack[-1] == num:
                # stack[-1] *= 2
                    stack.pop()
                    num = num * 2
                stack.append(num)
                # if len(stack) > 2:
                #     while stack[-1] == stack[-2]:
                #         stack.pop()
                #         stack[-1] *= 2
            else:
                stack.append(num)
        return stack
# [2,1,1,2]
# [2,2,2]
# [2,2,2]