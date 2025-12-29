class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        friends = set(friends)
        for rank in order:
            if rank in friends:
                res.append(rank)
        return res
