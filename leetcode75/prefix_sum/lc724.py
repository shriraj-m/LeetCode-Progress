"""724. Find Pivot Index"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for idx, num in enumerate(nums): # assign index counter for each val
            right -= num
            if left == right:
                return idx
            left += num

        return -1
