# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoSortedLinkedLists(list1, list2):
            dummy = ListNode(-1)
            temp = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            if list1 or list2:
                temp.next = list1 or list2
                # if list1:
                #     temp.next = list1
                # else:
                #     temp.next = list2
            return dummy.next

        def findMid(head):
            if not head or not head.next:
                return head

            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if not head or not head.next:
            return head

        mid = findMid(head)
        right = mid.next
        mid.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return mergeTwoSortedLinkedLists(left, right)
