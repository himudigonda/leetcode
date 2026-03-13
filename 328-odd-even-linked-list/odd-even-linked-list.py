# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even = head.next
        evenHead = head.next

        while odd and odd.next and even and even.next:
            if odd.next and odd.next.next:
                odd.next = even.next
                odd = odd.next

            if even.next and even.next.next:
                even.next = odd.next
                even = even.next

        even.next = None
        odd.next = evenHead

        return head
