"""206. Reverse Linked List"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            temp = head.next # save next value (ex, 1 -> 2 - save 2)
            head.next = node # does the flip by breaking connection (null <- 1 / 2)
            node = head # new node is current head (1 is now the node)
            head = temp # sets the head to 2 (head.next) which helps reconnect after
        return node