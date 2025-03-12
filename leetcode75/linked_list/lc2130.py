"""2130. Maximum Twin Sum of a Linked List"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ele = []
        result = 0
        while head:
            ele.append(head.val)
            head = head.next

        start,end = 0,len(ele)-1
        while start<end:
            result = (ele[start] + ele[end]) if (ele[start] + ele[end]) > result else result
            start += 1
            end -= 1
        return result