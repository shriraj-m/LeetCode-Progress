class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        # now make a function to do binary search on each side
        def bs(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
            return -1
                
        res = bs(0, pivot - 1)
        if res != -1:
            return res
        
        return bs(pivot, len(nums)-1)
        
