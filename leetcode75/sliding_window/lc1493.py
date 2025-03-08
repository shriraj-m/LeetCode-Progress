"""1493. Longest Subarray of 1's After Deleting One Element"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros, maxLength = 0,0,0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxLength = max(maxLength, right-left)
        return maxLength