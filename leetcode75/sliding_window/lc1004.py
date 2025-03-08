"""1004. Max Consecutive Ones III"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        # start with both pointers on same index
        for right in range(len(nums)):
            # if right is a 0, then take away 1 k
            if nums[right] == 0:
                k -= 1
            # if k is less than 0, we need to check if there are 0's at the left
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            right += 1
            # return distance between right and left
        return right - left