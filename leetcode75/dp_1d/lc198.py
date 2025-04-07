"""198. House Robber"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length

        if len(nums) == 1:
            return nums[0]
            
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            print(dp)

        return dp[-1]