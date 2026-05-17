"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval.start)

        prev_et = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prev_et:
                return False
            prev_et = intervals[i].end

        return True
