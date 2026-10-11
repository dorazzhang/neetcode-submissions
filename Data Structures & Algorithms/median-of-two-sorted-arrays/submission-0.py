class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        half = (len(A) + len(B)) // 2

        # code will search on A, we want that to be the smaller array
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1 # finding the partition for array A where left half is to the left of median, right half is to the right of median

        # you then know the partition for B as well by taking the remaining half of total length

        while True: # we know there's a solution at some point
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (len(A) + len(B)) % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1