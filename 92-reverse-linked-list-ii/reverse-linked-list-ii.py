# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # diff = right - left + 1
        dummy = ListNode(0, head)
        leftprev = dummy
        ptr = head

        for _ in range(left - 1):
            leftprev = ptr
            ptr = ptr.next

        prev = None
        stitch = ptr
        for i in range(right - left + 1):
            tmp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tmp

        leftprev.next.next = ptr
        leftprev.next = prev

        return dummy.next
