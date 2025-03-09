"""1207. Unique Number of Occurrences"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1

        key_occurances = len(set(hashmap.keys()))
        value_occurances = len(set(hashmap.values()))

        return key_occurances == value_occurances