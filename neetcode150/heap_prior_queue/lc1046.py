import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0]

        maxheap = stones
        while len(maxheap) > 1:
            heapq.heapify_max(maxheap)

            # now its in order
            # get x and y
            y = heapq.heappop(maxheap)
            heapq.heapify_max(maxheap)
            x = heapq.heappop(maxheap)

            if x != y:
                heapq.heappush(maxheap, y-x)

        if len(maxheap) == 1:
            return maxheap[0]
        else:
            return 0


        