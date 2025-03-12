"""2095. Delete the Middle Node of a Linked List"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: # no next value
            return None
        
        slow = head
        fast = head.next.next

        while fast and fast.next: # while both exist
            slow = slow.next
            fast = fast.next.next
        
        # one behind middle by now, so go next to get to middle
        # set that node to the next one to remove current middle.
        slow.next = slow.next.next
        return head