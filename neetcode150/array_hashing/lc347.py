"""TOP K FREQUENT ELEMENTS"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num -> freq
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # now sort count
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print(arr)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) # we want num value
        return res
