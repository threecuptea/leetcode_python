# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        # There is only one node, remove it and leave nothing.
        if head.next is None:
            return None
        dummy = ListNode(0, head)
        l, lp, r, rp = head, dummy, head, dummy
        while r.next:
            lp, l = l, l.next
            if r.next:
                rp, r = rp.next, r.next
                if r.next:
                    rp, r = rp.next, r.next
        lp.next = l.next
        l = None
        return dummy.next