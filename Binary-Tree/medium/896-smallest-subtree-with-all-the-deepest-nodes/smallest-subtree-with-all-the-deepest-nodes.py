# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None

        # depths = defaultdict(int)
        # parent = defaultdict(TreeNode)
        # q = deque([(root, 0)])
        # maxdepth = -1

        # while q:
        #     node, depth = q.popleft()
        #     depths[node] = depth
        #     maxdepth = max(maxdepth, depth)
        #     if node.left:
        #         q.append((node.left, depth + 1))
        #         parent[node.left] = node
        #     if node.right:
        #         q.append((node.right, depth + 1))
        #         parent[node.right] = node

        # maxes = [key for key, val in depths.items() if val == maxdepth]

        # while len(maxes) > 1:
        #     maxes = {parent[node] for node in maxes}
        # return list(maxes)[0]

        def dfs(node):
            if not node:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_node
            if right_depth > left_depth:
                return right_depth + 1, right_node
            return left_depth + 1, node

        return dfs(root)[1]
