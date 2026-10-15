# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        count = 1
        
        dummy = ListNode(0, head)
        prev = dummy

        while prev and count != left:
            prev = prev.next
            count += 1
        
        first = prev
        last = prev.next

        curr = prev.next

        while curr and count != right + 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        if first:
            first.next = prev
        if last:
            last.next = curr
        
        return dummy.next

                
        