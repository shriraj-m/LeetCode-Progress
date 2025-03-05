"""334. Increasing Triplet Subsequence"""              
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num # save first value if lower
            elif num <= second:
                second = num # save second value if lower
            else:
                return True # if this is reached, then a third value in order is greater
        return False
        