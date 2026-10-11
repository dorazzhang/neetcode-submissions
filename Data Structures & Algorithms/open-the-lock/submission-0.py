class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # lock w 4 circular wheels
        # 10 slots -> 0 - 9

        # starts at 0000
        # list of deadends, meaning for any of the codes it will break the lock

        # given password, return minimum turns to open the lock

        # 0000 -> 1000

        # have a node for every possible value 

        # make deadends a set

        # perform bfs on graph and return count when reach target
        # else return -1

        visited = set(deadends)

        if target == "0000":
            return 0
        if "0000" in visited:
            return -1

        queue = deque()
        queue.append("0000")
        visited.add("0000")
        turns = 0

        while queue:
            for _ in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for i in range(4):
                    for direction in [-1, 1]:
                        digit = str((int(lock[i]) + direction) % 10)
                        nextLock = lock[:i] + digit + lock[i + 1:]
                        if nextLock in visited:
                            continue
                        queue.append(nextLock)
                        visited.add(nextLock)
            turns += 1
        return -1
