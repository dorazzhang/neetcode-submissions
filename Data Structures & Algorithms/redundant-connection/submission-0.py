class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # connected, undirected graph with n nodes 1 - n
        # no cycles and n - 1 edges

        # add one additional edge w two different vertices

        # array of edges [ai, bi] (nodes ai and bi)

        # return edge that can be removed so graph is still connected, non-cyclical

        # if multiple answers, return edge that appears last in edges

        # dfs from first node and edges in order that they appear
        # if cycle forms from an edge, return that edge

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent: # for undirected graph, makes sure node is not going backwards (parent is the prev node that node came from)
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)

        for src, dst in reversed(edges):
            if src in cycle and dst in cycle:
                return [src, dst]
        
        return []





        
        