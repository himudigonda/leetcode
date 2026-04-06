class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        streaks = {}
        longest = 0

        for num in numset:
            l_streak = streaks.get(num - 1, 0)
            r_streak = streaks.get(num + 1, 0)
            streak = 1 + l_streak + r_streak

            streaks[num - l_streak] = streak
            streaks[num + r_streak] = streak
            longest = max(streak, longest)
        return longest
