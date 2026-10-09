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
        
        visited = set() # track already visited nodes
        cycle = set() # track nodes in cycle
        cycleStart = -1 # track the start of the cycle

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited: # if the node has been visited before, this is the start of the cycle
                cycleStart = node
                return True # true lets us know cycle is found
            visited.add(node) # visited node

            for neighbor in adj[node]: # continue to neighbors
                if neighbor == parent: # for undirected graph, makes sure node is not going backwards (parent is the prev node that node came from)
                    continue
                if dfs(neighbor, node): # if cycle detected
                    if cycleStart != -1: # if cycle hasn't ended yet
                        cycle.add(node) # add node to cycle
                    if node == cycleStart: # if cycle ends bc startNode was found again
                        cycleStart = -1 # end cycle
                    return True # cycle found
            return False # cycle not found
        
        dfs(1, -1)

        for src, dst in reversed(edges):
            if src in cycle and dst in cycle:
                return [src, dst]
        
        return []





        
        