# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        current = head.next
        head.next = None
        while current.next:
            nn = current.next
            current.next = prev
            prev = current
            current = nn
        current.next = prev
        return current
        

        