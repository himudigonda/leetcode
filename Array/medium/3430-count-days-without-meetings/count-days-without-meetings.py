class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prevend = 0
        meetings.sort()
        # for start, end in meetings:
        #     start = max(start, prevend + 1)
        #     length = end - start + 1
        #     days -= max(length, 0)
        #     prevend = max(prevend, end)
        # return days

        for start, end in meetings:
            if end <= prevend:
                continue
            elif start > prevend:
                days -= end - start + 1
            else:
                days -= end - prevend
            prevend = end
        return days
