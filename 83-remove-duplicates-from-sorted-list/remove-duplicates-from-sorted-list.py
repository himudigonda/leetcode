# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        left = head
        right = head.next
        
        while right:
            if left.val == right.val:
                right = right.next
                left.next = right
            else:
                left = right
                right = right.next
        return head