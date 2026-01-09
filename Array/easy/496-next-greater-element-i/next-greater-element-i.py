class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}

        # for all nums in nums2 arr
        for num in nums2:
            # while there are elements in the stack
            # and
            # the current number is larger that whats on the top of the stack
            while stack and num > stack[-1]:
                # put a new mapping of the element on top of the stack : current number
                # this is essentially staying current number is larger than the elements in the stack
                mapping[stack.pop()] = num
            # append the current number to the stack for finding elements larger that this
            stack.append(num)
        # by now you will have a mapping of next larger for each element

        while stack:
            # now we just say the ones in the stack still have no element larger than them,
            # so we put -1 for their mapping
            mapping[stack.pop()] = -1

        for num in nums1:
            # now we append the NGE from the mapping based on the ele in nums1
            res.append(mapping[num])

        return res
