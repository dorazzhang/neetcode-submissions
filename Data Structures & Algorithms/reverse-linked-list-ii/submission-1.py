# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # dummy node point to head
        dummy = ListNode(0, head)

        # prev is None and cur is our head
        leftPrev, cur = dummy, head

        # want to get to the node where we start reversing from
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next # leftprev will be the node right before the reverse

        # this prev handles our reversing, None at first bc we want to break its link w non reversed part
        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # now the first node that was reversed needs to point to the non reversed node after right
        leftPrev.next.next = cur
        # node before reversed portion points to last reversed node
        leftPrev.next = prev

        # return list with our dummy node
        return dummy.next