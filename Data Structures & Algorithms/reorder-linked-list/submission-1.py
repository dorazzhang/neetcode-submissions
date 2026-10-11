# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # reorder into 0, n - 1, 1, n - 2, n - 3

        # [0 1 2]
        # [6 5 4 3] <- reverse this one

        # fast and slow pointers gives you midpoint

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr2 = slow.next
        slow.next = None


        prev = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        
        curr1 = head
        curr2 = prev

        while curr2:
            next1 = curr1.next
            next2 = curr2.next

            curr1.next = curr2
            curr2.next = next1

            curr1 = next1
            curr2 = next2


        