class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            # prereq is [a, b]
            # for course index b, its neighbor is a because you must take b before going to a
            adjList[prereq[1]].append(prereq[0])
            
        # run through dfs, return false if cycle is detected, continue if cycle not detected, return true when complete
        
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            state[course] = 1
            for next in adjList[course]:
                if dfs(next):
                    continue
                else:
                    return False
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

            