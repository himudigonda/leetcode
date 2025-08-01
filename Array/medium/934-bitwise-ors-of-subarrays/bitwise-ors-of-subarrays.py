class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # # Iter1
        # distinctSet = set()
        # curSet = set()
        # for num in arr:
        #     curSet = {num | x for x in curSet} | {num}
        #     distinctSet |= curSet
        # return len(distinctSet)

        # # BruteForce
        # distinct_ors = set()
        # n = len(arr)
        # for i in range(n):
        #     current_or = 0
        #     for j in range(i, n):
        #         current_or |= arr[j]
        #         distinct_ors.add(current_or)
        # return len(distinct_ors)

        # Optimal
        distinctSet = set()
        curSet = set()
        for x in arr:
            newCurSet = {x}
            for prevOr in curSet:
                newCurSet.add(prevOr | x)
            curSet = newCurSet
            distinctSet.update(curSet)
        return len(distinctSet)