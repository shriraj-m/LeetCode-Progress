"""2542. Maximum Subsequence Score"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        totalSum = 0
        heap = []

        merged = list(zip(nums2, nums1))
        merged.sort(reverse=True)
        print(merged)

        for minOf2, num1Val in merged:
            # if length of heap is same as k, then take away min value in heap
            if len(heap) == k:
                totalSum -= heapq.heappop(heap)

            totalSum += num1Val
            heapq.heappush(heap, num1Val)

            if len(heap) == k:
                result = max(result, totalSum * minOf2)

        return result