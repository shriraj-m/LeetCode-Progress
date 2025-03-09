"""2215. Find the Difference of Two Arrays"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer.append(list((set(nums1) - set(nums2))))
        answer.append(list((set(nums2) - set(nums1))))
        return answer  




