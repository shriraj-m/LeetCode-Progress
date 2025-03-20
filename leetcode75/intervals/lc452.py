"""452. Minimum Number of Arrows to Burst Balloons"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        stack = []
        for start, end in points:
            if len(stack) > 0 and stack[-1][1] >= start:
                last_start, last_end = stack.pop()
                stack.append([max(start, last_start), min(end, last_end)])
            else:
                stack.append([start, end])
        return len(stack)
