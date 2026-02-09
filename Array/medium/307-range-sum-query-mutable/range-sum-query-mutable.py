class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        def makeTree(nums, l, r):
            if l > r:
                return None

            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node

            mid = (l + r) >> 1
            node = Node(l, r)
            node.left = makeTree(nums, l, mid)
            node.right = makeTree(nums, mid + 1, r)
            node.total = node.left.total + node.right.total
            return node

        self.root = makeTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def rec_update(node, idx, val):
            if node.start == node.end:
                node.total = val
                return node

            mid = (node.start + node.end) >> 1
            if idx <= mid:
                rec_update(node.left, idx, val)
            else:
                rec_update(node.right, idx, val)
            node.total = node.left.total + node.right.total
            return node.total

        return rec_update(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def findsumofrange(node, left, right):
            if node.start == left and node.end == right:
                return node.total
            mid = (node.start + node.end) >> 1
            if right <= mid:
                return findsumofrange(node.left, left, right)
            elif left >= mid + 1:
                return findsumofrange(node.right, left, right)
            else:
                return findsumofrange(node.left, left, mid) + findsumofrange(
                    node.right, mid + 1, right
                )

        return findsumofrange(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
