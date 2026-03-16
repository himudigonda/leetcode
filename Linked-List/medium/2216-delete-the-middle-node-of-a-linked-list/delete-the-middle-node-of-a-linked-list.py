# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = head
        # ptr = dummy

        while fast and fast.next:
            slow = slow.next
            # ptr = ptr.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next
