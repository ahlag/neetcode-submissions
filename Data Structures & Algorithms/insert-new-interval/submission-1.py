class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda pairs: pairs[0])
        output = [intervals[0]]

        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])

        return output
