# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        right = head
        while right and right.next:
            right = right.next.next
            left = left.next
        # 1->2->3->4
        #       l
        #             r
        prev = None
        cur = left
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # 1->2->
        # 
        # None <- 3<-4
        #            p c
        
        headhead = head
        while headhead and prev :
            if headhead.val == prev.val:
                headhead = headhead.next
                prev = prev.next
            else:
                return False
        return True
