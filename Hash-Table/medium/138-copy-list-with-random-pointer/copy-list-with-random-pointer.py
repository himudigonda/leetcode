"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # # HashMap Solution: O(n), O(n)
        # mapping = {}
        # cur = head

        # while cur:
        #     mapping[cur] = Node(cur.val)
        #     cur = cur.next

        # cur = head
        # while cur:
        #     mapping[cur].next = mapping.get(cur.next)
        #     mapping[cur].random = mapping.get(cur.random)
        #     cur = cur.next

        # return mapping[head]

        # Direct Interweaving: O(n), O(1)
        cur = head
        while cur:
            newnode = Node(cur.val, cur.next)
            cur.next = newnode
            cur = newnode.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        oldhead = head
        newhead = head.next
        curold = oldhead
        curnew = newhead

        while curold:
            curold.next = curold.next.next
            curnew.next = curnew.next.next if curnew.next else None
            curold = curold.next
            curnew = curnew.next if curnew.next else None

        return newhead
