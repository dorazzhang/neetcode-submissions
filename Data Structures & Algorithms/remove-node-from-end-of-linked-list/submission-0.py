# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head

        length = 0
        while curr:
            curr = curr.next
            length += 1
        count = length - n

        if count == 0:
            return head.next
        curr = head
        for i in range(count - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head

        