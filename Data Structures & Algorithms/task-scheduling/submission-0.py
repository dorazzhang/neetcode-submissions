class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks : input A-Z
        # n
        #cpu cycle allows completion of one task, any order
        # identical tasks have to be separated by at least n cycles

        # x x y y n = 2
        # x y idle x y

        # intuition: highest frequency ones should start first
        # A _ _ _ A _ _ _ A
        # some kind of system like a queue?
        
        # sort by frequency and do most frequent first
        # store task with its cooldown

        # need to do high frequency ones first, and also do them immdiately once cooled down

        # max heap store task, count # only of ones that are cooleddown
        # if not cooled down, put it in a queue with n padding in between
        # so then every cycle, you pop from queue and add back to heap if its a valid task
        
        freq = defaultdict(int) # frequencies of all tasks
        for t in tasks:
            freq[t] += 1
        
        heap = []
        for task, count in freq.items():
            heapq.heappush(heap, (-1 * count, task)) # -frequencies bc max heap
        
        queue = deque()

        res = 0

        while heap or queue:
            if queue:
                possible_count, possible_task = queue.popleft()
                if possible_task != '#':
                    heapq.heappush(heap, (possible_count, possible_task))
            
            if heap:
                count, task = heapq.heappop(heap)
                count += 1 # decrement negative task (ie. -2 -> -1)
                if count != 0:
                    while len(queue) < n:
                        queue.append((0, '#'))
                    queue.append((count, task))
            res += 1
        
        return res