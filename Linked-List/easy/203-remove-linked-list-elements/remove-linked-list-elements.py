# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy.next
        prev = dummy

        while cur:
            while cur and cur.val == val:
                cur = cur.next
            prev.next = cur
            prev = cur
            if cur:
                cur = cur.next
        return dummy.next
