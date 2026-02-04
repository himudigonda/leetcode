# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        if not root:
            return []

        triple_to_id = defaultdict(int)
        id_counts = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # curstr = f"({left}),{node.val},({right})"
            triple = (left, node.val, right)
            # curstr = str(left) + "," + str(node.val) + "," + str(right)

            if triple not in triple_to_id:
                triple_to_id[triple] = len(triple_to_id) + 1
            cur_id = triple_to_id[triple]
            id_counts[cur_id] += 1

            if id_counts[cur_id] == 2:
                res.append(node)
            return cur_id

            # mapping[curstr] += 1
            # if mapping[curstr] == 2:
            #     res.append(node)
            # return curstr

        dfs(root)
        return res
