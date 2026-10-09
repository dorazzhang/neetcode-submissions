class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # beginWord, endWord
        # list of words wordList
        # same length, lowercase, distinct
        # transform beginWord into endWord 
        # using any word in wordList one char at a time
        # minimum number of words to obtain endWord

        # can create a graph corresponding word with patterns
        # for example dog -> *og, d*og, do*
        # any word that shares one of these patterns is a valid transform
        # for example dot -> do*

        # graph stores pattern -> words

        # store beginword in queue
        # pop from queue, get patterns
        # loop through dict[patterns] and add non visited words to queue
        # bfs for shortest distance

        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:] # slicing never goes out of bounds, just returns nothing
                adj[pattern].append(word)
        
        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)
        count = 1

        while queue:
            for n in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return count
                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + "*" + curr_word[i + 1:]
                    for word in adj[pattern]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)
            count += 1
        
        return 0


        
        