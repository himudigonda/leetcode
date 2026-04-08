class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        vis = [False] * numCourses
        path = [False] * numCourses

        def dfs(node):
            vis[node] = path[node] = True
            
            for nextnode in adj[node]:
                if not vis[nextnode]:
                    if dfs(nextnode): return True
                elif path[nextnode]: return True

            path[node] = False
            return False
            

        for i in range(numCourses):
            if not vis[i]:
                if dfs(i): return False
        return True