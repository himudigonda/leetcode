# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        left = headA
        right = headB
        seen = set()
        while left:
            seen.add(left)
            left = left.next

        while right:
            if right in seen:
                intersection_node = right
                value = intersection_node.val
                print(value)
                return right

            seen.add(right)
            right = right.next
        return None
