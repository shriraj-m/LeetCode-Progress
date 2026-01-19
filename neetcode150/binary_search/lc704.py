class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = int((r+l)/2)
        
        for _ in nums:
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target: 
                r = mid
            elif nums[mid] < target:
                l = mid+1
            
            # recalc mid
            mid = int((l+r)/2)
        return -1
        