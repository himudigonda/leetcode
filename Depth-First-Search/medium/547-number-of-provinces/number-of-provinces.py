class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(idx, adj_list, visited):
            visited.add(idx)
            for i in adj_list[idx]:
                if i not in visited:
                    dfs(i, adj_list, visited)
            return

        n = len(isConnected)
        adj_list = [[] for _ in range(n)]
        counts = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)

        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, adj_list, visited)
                counts += 1
        return counts
