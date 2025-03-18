"""875. Koko Eating Bananas"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        def canEatAll(piles, speed, h):
            # speed is the  middle pile.
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            print(f"checking speed {speed}, with a result of {hours} hrs")
            return hours <= h

        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            print(f"current vals: left {left} | right {right} | mid {mid}")
            if canEatAll(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left
