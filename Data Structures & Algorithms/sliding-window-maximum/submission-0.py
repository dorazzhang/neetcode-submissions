class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max1 = nums[0]
        # max2 = nums[0]
        # for i in range(k):
        #     if nums[i] > max1:
        #         max2 = max1
        #         max1 = nums[i]
        #     elif nums[i] > max2:
        #         max2 = nums[i]
        # res = []
        # res.append(max1)
        # l = 0
        # for r in range(k, len(nums)):
        #     if nums[l] == max1 and max2 > nums[r]:
        #         res.append(max2)
        #         max1 = max2

        #     elif nums[l] == max1 and max2 <= nums[r]:
        #         res.append(nums[r])
        #         max2 = max1
        #         max1 = nums[r]
        #     else:
        #         res.append(max1)
        #         if max2 < nums[r]:
        #             max2 = nums[r]

        #     l += 1
        # return res

        # doesn't work because there's cases where you will need to know the 3rd max of the sliding window when both 1 and 2 of the original are gone...

        # need to maintain a sorted array of length k for every window (but only modify the last and first values)

        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
