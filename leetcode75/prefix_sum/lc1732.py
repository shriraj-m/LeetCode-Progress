"""1732. Find the Highest Altitude  """
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0 # starts at 0
        highest_height = 0 # track highest height, start at 0.

        for value in gain:
            # calculate changes in altitude
            current += value
            highest_height = max(highest_height, current)
        
        return highest_height