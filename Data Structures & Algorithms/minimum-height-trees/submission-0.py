class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # undirected graph two vertices are connected by one path
        # tree of n nodes 0 to n - 1
        # array of n - 1 edges
        # can choose any node as root
        # return list of mht root labels
        # for a tree of n nodes, its min heigh should be logn?

        # can try bfs on every root and store the height and root
        # would be slow, V(V+E)

        # for one node, height one
        # for two nodes, height still one
        # for three nodes, the middle node as root would optimize it
        # if you add nodes to the middle, the height wouldnt change
        # basically can go from outer layers to finding the centroid
        # leaf nodes (with only one edge) cannot be the center

        # will only be at most 2 roots that do this

        if n == 1:
            return [0]

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        edge_count = {}
        leaves = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)
                

