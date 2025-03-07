"""11. Container With Most Water"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # calculate width and height for area
            width = right - left
            max_area = max(max_area, (width) * min(height[left], height[right]))
            # shift pointers based on which one is smaller
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area