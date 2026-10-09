class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbors in adj[node]:
                dfs(neighbors)
            return 

        components = 0
        for node in range(len(adj)):
            if node not in visit:
                dfs(node)
                components += 1
        
        return components