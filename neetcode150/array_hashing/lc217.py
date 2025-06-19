class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for num in nums:
            if num in hashmap:
                return True
            hashmap.add(num)
        return False