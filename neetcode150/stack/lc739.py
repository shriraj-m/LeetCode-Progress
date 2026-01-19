class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp, day
        # create result array the size of temperatores
        result = [0] * len(temperatures)

        # enumerate to get day and temperatore
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackD = stack.pop()
                result[stackD] = day - stackD
            stack.append((temp, day))
        return result