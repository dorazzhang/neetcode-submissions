# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # remove nth node from end of list and return head

        # can loop through once and count number of nodes in list
        # then we calculate length - n

        # loop through again and set pointers to None to remove node

        length = 0
        curr = head
        [0, 1, 2] # 1, 2, 3
        while curr:
            length += 1
            curr = curr.next
        
        ith = length - n
        if ith == 0:
            return head.next

        count = 0
        curr = head
        prev = None
        while curr:
            if count == ith:
                if prev:
                    prev.next = curr.next
                curr.next = None
                break
            prev = curr
            curr = curr.next
            count += 1
        
        return head
