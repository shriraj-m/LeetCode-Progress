"""435. Non-overlapping Intervals"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        # sort intervals based on second element
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                count += 1
            else:
                prev_end = intervals[i][1]
        return count