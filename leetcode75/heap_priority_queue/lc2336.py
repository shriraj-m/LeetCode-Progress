"""2336. Smallest Number in Infinite Set"""
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        values = []
        for x in range(1,1001):
            values.append(x)
        self.heap = values

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num in set(self.heap):
            return
        else:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
