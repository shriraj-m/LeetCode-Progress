"""739. Daily Temperatures"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res
