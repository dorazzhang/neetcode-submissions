class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] means must take course b before a (b is a prereq of a)
        # total numCourses you must take (0 to numCourses - 1)
        # true if possible to finish all courses
        # otherwise false

        # want to start from a course with no prereqs, if this doesnt exist, then it wouldnt work
        # cant have cycles a -> b -> c -> a
        # 1, 2 -> 3 3 to take 4
        # (1, 2) (3) (4)

        # first create your graph of courses, where you point prereq to corresponding class (adj list)
        # at the same time, you want to track the indegree of every course
        # an indegree of 0 means 0 edges going into the node aka zero prereqs
        # run bfs by initializing queue as nodes with indeg=0 
        # decrement indeg of neighboring nodes when processing and add them to queue if they become 0 as well (meaning all prereqs were taken)

        adj = defaultdict(list) # prereq : courses they are a prereq for
        indeg = defaultdict(int) # course : indegree count
        processed = set()

        for c, p in prerequisites:
            adj[p].append(c)
            indeg[c] += 1

        queue = deque()
        
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            processed.add(course)
            for nei in adj[course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        return len(processed) == numCourses

            