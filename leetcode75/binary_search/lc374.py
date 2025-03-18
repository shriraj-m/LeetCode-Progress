"""374. Guess Number Higher or Lower"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search utilizes halves, so we can make that work. 
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2 # floor division
            print(mid)
            result = guess(mid)

            if result == 0: # we guessed right
                return mid
            
            if result == 1: # we guessed too low
                # move low value to mid+1
                low = mid+1
            else: # too high
                high = mid-1
