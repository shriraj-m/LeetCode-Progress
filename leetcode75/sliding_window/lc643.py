"""643. Maximum Average Subarray I"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum 

        # iterate starting at k
        for i in range(k, len(nums)):
            print(i)
            # add the element on right, remove element on left (sliding window)
            cur_sum += nums[i] - nums[i-k]

            # determine new max
            max_sum = max(max_sum, cur_sum)
        
        return max_sum / k