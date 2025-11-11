# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    #####
    # 2. Add Two Numbers
    # https://leetcode.com/problems/add-two-numbers/description/
    #####
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val # l1, l2 has len >= 1
        head = ListNode(val % 10)
        prev, l1, l2, val = head, l1.next, l2.next, val // 10 # carry over
        while l1 or l2:
            # 'val' stores the sum of carrier, l1.val and l2.val, then re-used as carrier for the next loop
            if l1:
                val, l1 = val + l1.val, l1.next
            if l2:
                val, l2 = val + l2.val, l2.next
            prev.next = ListNode(val % 10)
            prev, val = prev.next, val // 10
        # Don't forget that there might be a carrier at the end
        if val == 1:
            prev.next = ListNode(1)
        return head