class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # town judge trusts nobody
        # everybody trusts the judge
        # find the node that has no neighbors and is the neighbor of all in a graph

        trustees = defaultdict(int)
        trusters = defaultdict(int)

        for a, b in trust:
            trusters[b] += 1
            trustees[a] += 1 # a trusts b
        
        for person in range(1, n + 1):
            if trusters[person] == n - 1 and person not in trustees:
                return person
        
        return -1
