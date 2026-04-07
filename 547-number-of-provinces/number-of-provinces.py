class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjlist = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adjlist[i].append(j)

        def dfs(i):
            seen.add(i)
            for i in adjlist[i]:
                if i not in seen:
                    dfs(i)
            return

        seen = set()
        count = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1
        return count
