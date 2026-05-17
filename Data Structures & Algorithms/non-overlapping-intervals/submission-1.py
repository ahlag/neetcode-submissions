class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[1])

        removed = 0
        prev_end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            start_time, end_time = intervals[i]

            if start_time < prev_end_time:
                removed += 1
            else:
                prev_end_time = end_time

        return removed

        