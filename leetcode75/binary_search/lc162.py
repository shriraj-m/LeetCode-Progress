"""162. Find Peak Element"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            print(f"current vals: mid = {mid}, left = {left}, right = {right}")
            if nums[mid] < nums[mid+1]: # current is less than its neighbors.
                left = mid+1
            else:
                right = mid
        return left
