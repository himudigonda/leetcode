# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # # Set based solution
        # left = headA
        # right = headB
        # seen = set()
        # while left:
        #     seen.add(left)
        #     left = left.next

        # while right:
        #     if right in seen:
        #         intersection_node = right
        #         value = intersection_node.val
        #         print(value)
        #         return right

        #     seen.add(right)
        #     right = right.next
        # return None

        # Pointer inverting
        left = headA
        right = headB

        while left != right:
            left = left.next if left else headB
            right = right.next if right else headA
        return left
