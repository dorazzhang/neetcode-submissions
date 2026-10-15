class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # only has a, b, c
        # no aaa bbb ccc
        # at most a of a
        # at most b of b
        # etc ...

        #longest possible happy string

        # max possible length is a + b + c
        # min length is 0

        # binary search? seems a little hard to get the condition bc u have to build the valid string to check

        # otherwise i would try to split up like a = 3, b = 4, c = 2
        # a b c a b c -> out of c
        # a b c a b c a b -> out of a
        # a b c a b c a b b when would this strat be non optimal

        # would want greatest freq to go first and use up two

        # b b 
        # b b a b b a a c c

        # b = 2, c = 6

        #cc b cc b cc
        # vs 
        # cc bb cc

        # b = 4, c = 6 ohh basically keep adding the most freq one unless it makes a three, then i take the second most freq

        # cc b cc b cc bb

        # heap? would be nlog3

        max_heap = []
        if a:
            heapq.heappush(max_heap, (-a, 'a'))
        if b:
            heapq.heappush(max_heap, (-b, 'b'))
        if c:
            heapq.heappush(max_heap, (-c, 'c'))

        res = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)

            if len(res) >= 2:
                if res[-1] == char and res[-2] == char:
                    if not max_heap:
                        break
                    new_freq, new_char = heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (freq, char))
                    char, freq = new_char, new_freq
            
            freq = -freq
            res.append(char)
            freq -= 1

            if freq > 0:
                heapq.heappush(max_heap, (-freq, char))

        return "".join(res)

