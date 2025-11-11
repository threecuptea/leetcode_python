from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #####
    # 92. Reverse Linked List II
    # https://leetcode.com/problems/reverse-linked-list-ii/description/
    # Inspired by https://www.youtube.com/watch?v=RF_M9tX4Eag
    #####
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(0, head)  # The reverse can start with position 1. Therefore, we keep dummy for edge cases.
        prev, curr = dummy, head
        # Since we will use prev, curr, next for reverse operation.  Therefore, use those pointers.
        # Straight move to the left position (left -1) move
        for i in range(left-1):
            curr, prev = curr.next, curr
        lp, prev = prev, None  # lp for the node prior to the left position for pointer assignment
        # reverse between left and right
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        # prev is at the right to position, curr is at the one following the right position
        lp.next.next = curr # this need to come first before reassignment
        lp.next = prev
        return dummy.next