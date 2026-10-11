class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # # a : b
        # # b : c

        # # build graph if directed edges from prereq to course

        # # graph has edges between all prereqs and their courses
        # # if you can get from a course to another course then its a prereq

        # # helper function returning if you can get from src to dst
        # def possiblePath(src, dst, graph):
        #     queue = deque()
        #     queue.append(src)
        #     visited = set()
        #     visited.add(src)

        #     while queue:
        #         course = queue.popleft()
        #         if course == dst:
        #             return True
        #         for nextCourse in graph[course]:
        #             if nextCourse not in visited:
        #                 queue.append(nextCourse)
        #                 visited.add(nextCourse)
            
        #     return False


        # graph = defaultdict(list)

        # for p in prerequisites:
        #     graph[p[0]].append(p[1])
        
        # res = []
        # for q in queries:
        #     res.append(possiblePath(q[0], q[1], graph))
        
        # return res

        # build adjacency list and compute the indegree for each course
        # start a queue with all courses with indegree of zero
        # for every course, its neighbors will get the course itself and its prereqs appended

        # then for every query, we check the set for that course

        prereqs = defaultdict(set) # stores course : its prereqs
        adj = defaultdict(list) # stores direct prereq -> course
        indegree = defaultdict(int)

        for p in prerequisites:
            adj[p[0]].append(p[1])
            indegree[p[1]] += 1
        
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            for nextCourse in adj[course]:
                prereqs[nextCourse].update(prereqs[course])
                prereqs[nextCourse].add(course)
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        

        res = []
        for q in queries:
            res.append(q[0] in prereqs[q[1]])
        
        return res
