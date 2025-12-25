class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        twodigit = n - 1
        onedigit = m - 1
        onezero = m + n - 1

        while twodigit >= 0:
            if onedigit >= 0 and nums1[onedigit] > nums2[twodigit]:
                nums1[onezero] = nums1[onedigit]
                onedigit -= 1
            else:
                nums1[onezero] = nums2[twodigit]
                twodigit -= 1
            onezero -= 1
        return nums1
