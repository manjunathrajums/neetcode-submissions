# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        nn = head
        if not head or not head.next:
            return False
        
        if nn.next:
            while nn.next:
                if nn.next in seen:
                    return True
                else:
                    seen.add(nn.next)
                nn = nn.next
        return False

        