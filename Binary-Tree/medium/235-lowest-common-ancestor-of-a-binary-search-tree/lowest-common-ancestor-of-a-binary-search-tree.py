# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # # BST Method
        # while root:
        #     if p.val > root.val and q.val > root.val:
        #         root = root.right
        #     elif p.val < root.val and q.val < root.val:
        #         root = root.left
        #     else:
        #         return root

        # Recursion
        if not root:
            return root

        def find(node):
            if not node or node == p or node == q:
                return node

            left = find(node.left)
            right = find(node.right)

            if left and right:
                return node
            else:
                return left or right

        return find(root)
