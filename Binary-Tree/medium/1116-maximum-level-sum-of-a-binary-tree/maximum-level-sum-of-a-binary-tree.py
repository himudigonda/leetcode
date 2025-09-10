# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # # Brute Force
        # level_no = 1
        # max_sum = root.val
        # level = [root]
        # max_level = 1

        # while level:
        #     next_level = []
        #     level_sum = 0

        #     for node in level:
        #         level_sum += node.val
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     if level_sum > max_sum:
        #         max_sum = level_sum
        #         max_level = level_no
        #     level = next_level
        #     level_no += 1
        # return max_level

        # BFS with queue
        q = deque([root])
        best_sum = float("-inf")
        best_level = 1
        level = 1

        while q:
            q_len = len(q)
            level_sum = 0
            for _ in range(q_len):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level
            level += 1
        return best_level
