class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # BruteForce
        # nums1idx = {n: i for i, n in enumerate(nums1)}
        # res = [-1] * len(nums1)
        # stack = []

        # for i in range(len(nums2)):
        #     cur = nums2[i]
        #     while stack and cur > stack[-1]:
        #         val = stack.pop()
        #         idx = nums1idx[val]
        #         res[idx] = cur
        #     if cur in nums1idx:
        #         stack.append(cur)
        # return res

        # Optimal
        stack = []
        d = {}
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)

        for num in stack:
            d[num] = -1
        return [d[x] for x in nums1]
