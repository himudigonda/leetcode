# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        mainptr = slow
        prev = None
        while mainptr:
            nxt = mainptr.next
            mainptr.next = prev
            prev = mainptr
            mainptr = nxt

        # iterate and check
        mainptr = head
        while mainptr and mainptr.next:
            if mainptr.val == prev.val:
                mainptr = mainptr.next
                prev = prev.next
            else:
                return False

        return True
