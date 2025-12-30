# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def calGCD(num1, num2):
            return math.gcd(num1, num2)

        def insertBetween(leftNode, rightNode, val):
            leftNode.next = ListNode(val, rightNode)
            return leftNode.next

        cur = head
        while cur and cur.next:
            val1 = cur.val
            val2 = cur.next.val

            gcd = calGCD(val1, val2)
            new_node = insertBetween(cur, cur.next, gcd)
            cur = new_node.next

        return head
