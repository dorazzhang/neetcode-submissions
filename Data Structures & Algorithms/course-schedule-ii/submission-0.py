class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build adjacency list of courses and their prereqs
        # so that the prereq points to the course its a prereq for

        # start at a node with no prereqs? how would you know that..

        # a -> b -> c
        # a: b
        # b : c

        # or try every node as the root and return the first path that contains no cycles and reaches every node

        # dfs where you add a course to result after all prereqs have been processed

        # [0, 1] first take course 1 to take course 0

        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0: # courses with no prereqs
                queue.append(i)

        res = []
        courses = 0
        while queue:
            course = queue.popleft()
            res.append(course)
            courses += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        return res if courses == numCourses else []
            




        