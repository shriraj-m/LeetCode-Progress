class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float('inf')

        while l <= r:
            # check if left is smaller than right
            if nums[l] < nums[r]:
                # already sorted, check nums[l]
                res = min(res, nums[l])

            mid = (r+l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                # check right if left-most is lower than mid
                l = mid + 1
            else:
                r = mid - 1

        return res