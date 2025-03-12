"""328. Odd Even Linked List"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        odd = head # pointer to first node as stated
        even = head.next # pointer to second node as stated
        even_head = even # the head of even which is the start

        while even and even.next: # while both even and even.next exist
            # set the one after odd to be the next odd number, same with even
            odd.next = odd.next.next
            even.next = even.next.next
            # moves odd to the next number, same with even
            odd = odd.next
            even = even.next
        # set next odd (aka nothing) to the starting even head
        odd.next = even_head
        return head
