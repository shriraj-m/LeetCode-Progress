"""GROUP ANAGRAMS"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(item)) for item in strs]
        print(sorted_strs)

        hashmap = {} # sorted string : list of real str

        for index, item in enumerate(sorted_strs):
            if item not in hashmap:
                hashmap[item] = [strs[index]]
            else: # item is in hashmap, so append
                hashmap[item].append(strs[index])

        # now use hashmap to create result
        result = []
        for item in hashmap:
            result.append(hashmap[item])
        
        print(result)
        return result