from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#####
# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# Use Floyd's Cycle-Finding Algorithm.  It is much faster
#####
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # slow move step and fast move two steps
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False