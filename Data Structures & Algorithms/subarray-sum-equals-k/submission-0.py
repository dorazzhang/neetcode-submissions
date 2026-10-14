class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums, k -> return total numbver of subarrays whose sum = k
        
        # 1 <= nums.length <= 20,000
        # -10,000,000 <= k <= 10,000,000

        # sliding window, maintaining a valid window where sum of elements in the window = k

        # right and left pointer both starting at 0
        # right pointer will increment by 1 while incrementing sum
        # when we reach a sum equal to k, we increment counter by one
        # while sum is too big, we increment left pointer

        # this only works for positive numbers

        # [0, 2, 1, 2, 4]

        # prefix - complement = sum (k)
        # prefix - k = complement

        # [2], [2,-2,1], [-1,1,2], [2]

        # calculate prefix array
        # iterate through and store in a hashmap the values we've seen and their frequency count
        # then at every index, we check if k complement exists in hasmap, and if it does, increment count by the frequency

        prefix = [0]
        total = 0
        count = 0

        for num in nums:
            total += num
            prefix.append(total)
        
        freq = defaultdict(int)
        freq[0] = 1
        
        for i in range(1, len(prefix)):
            if (prefix[i] - k) in freq:
                count += freq[prefix[i] - k]
            freq[prefix[i]] += 1
        
        return count
