class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # # traverse and merge
        # res = []
        # i = 0
        # n = len(intervals)

        # while i < n and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1

        # while i < n and intervals[i][0] <= newInterval[1]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)

        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res


        # append, sort and merge
        intervals.append(newInterval)
        intervals.sort()

        prev = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res