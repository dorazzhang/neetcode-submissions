class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # a : b
        # b : c

        # build graph if directed edges from prereq to course

        # graph has edges between all prereqs and their courses
        # if you can get from a course to another course then its a prereq

        # helper function returning if you can get from src to dst
        def possiblePath(src, dst, graph):
            queue = deque()
            queue.append(src)
            visited = set()
            visited.add(src)

            while queue:
                course = queue.popleft()
                if course == dst:
                    return True
                for nextCourse in graph[course]:
                    if nextCourse not in visited:
                        queue.append(nextCourse)
                        visited.add(nextCourse)
            
            return False


        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        res = []
        for q in queries:
            res.append(possiblePath(q[0], q[1], graph))
        
        return res
