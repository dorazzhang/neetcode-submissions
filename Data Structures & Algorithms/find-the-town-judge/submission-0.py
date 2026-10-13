class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # town judge trusts nobody
        # everybody trusts the judge
        # find the node that has no neighbors and is the neighbor of all in a graph

        adj = defaultdict(list)
        count = defaultdict(int)

        for a, b in trust:
            count[b] += 1
            adj[a].append(b) # a trusts b
        
        for person in range(1, n + 1):
            if count[person] == n - 1 and person not in adj:
                return person
        
        return -1
