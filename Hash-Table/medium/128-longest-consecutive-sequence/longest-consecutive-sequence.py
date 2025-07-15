class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force
        if not nums:
            return 0

        numset = set(nums)
        curnum = 0
        curstreak = 0
        longeststreak = 0

        for num in numset:
            if num - 1 not in numset:
                curnum = num
                curstreak = 1
            while curnum + 1 in numset:
                curnum += 1
                curstreak += 1
            longeststreak = max(longeststreak, curstreak)

        return longeststreak
