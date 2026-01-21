# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                # if l1 is less than l2, make it next and move forward
                node.next = list1
                list1 = list1.next
            else:
                # l2 is less than l1, so same here
                node.next = list2
                list2 = list2.next
            # move forward
            node = node.next
        node.next = list1 or list2
        return res.next
