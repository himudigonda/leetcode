# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = head
        fast = head
        ptr = dummy

        while fast and fast.next:
            slow = slow.next
            ptr = ptr.next
            fast = fast.next.next

        ptr.next = slow.next
        del slow
        return dummy.next
