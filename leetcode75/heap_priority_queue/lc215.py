"""215. Kth Largest Element in an Array"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # nums is now a heapq, if we want the k^th 
        # we can pop len of nums - k^th times., then return next pop
        removables = len(nums) - k
        for _ in range(removables):
            heapq.heappop(nums)

        return heapq.heappop(nums)            