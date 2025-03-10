"""933. Number of Recent Calls"""
from collections import deque

class RecentCounter:
    def __init__(self):
       self.q = deque() # use deque to have access to both sides. 

    def ping(self, t: int) -> int:
        queue = self.q
        queue.append(t)
        while queue[0] < t - 3000: # if value is outside of range (seeing if its less)
            queue.popleft()
        return(len(queue))



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

