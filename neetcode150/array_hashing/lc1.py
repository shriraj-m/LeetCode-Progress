"""TWO SUM"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index
        
        for i, n in enumerate(nums): # enumerate gives indx and val
            diff = target - n
            if diff in hashmap: # if the difference is already there, since diff is another num
                return [hashmap[diff], i] # return the diff pos + indx
            hashmap[n] = i # otherwise, add it
        