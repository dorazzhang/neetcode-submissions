class Twitter:

    def __init__(self):
        # map of user to followed users
        # store all tweets in by most recent

        self.followers = defaultdict(set)
        self.tweets = []
        self.time = -1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # publish new tweet with ID, user
        heapq.heappush(self.tweets, [self.time, userId, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get 10 most recent
        # check if user follows them, if not just skip that post
        posts = []
        seen = []
        while self.tweets and len(posts) < 10:
            time, user, tweet = heapq.heappop(self.tweets)
            if user in self.followers[userId] or user == userId:
                posts.append(tweet)
            seen.append([time, user, tweet])
        
        for saw in seen:
            heapq.heappush(self.tweets, saw)
        
        return posts


    def follow(self, followerId: int, followeeId: int) -> None:
        # user 1 follows user 2
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # user 1 unfollows user 2
        # remove from map
        self.followers[followerId].discard(followeeId)


