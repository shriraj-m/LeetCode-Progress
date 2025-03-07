"""1679. Max Number of K-Sum Pairs"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sorting the array allows us to find pairs of numbers that sum up to k.
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            if (nums[left] + nums[right]) == k:
                result += 1
                left += 1
                right -= 1
            elif (nums[left] + nums[right]) < k:
                left += 1
            else:
                right -= 1
        return result