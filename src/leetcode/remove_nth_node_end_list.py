from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ########
    # 19. Remove Nth Node From End of List
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
    # In genera, keep l, r pointer if rotate or remove nodes are involved.
    # r points to the last node.  The l points for the node before the target or the rotation
    # l and r has the k or n distance apart.
    # if the head is subject to change (the edge case), add dummy node for easy programming
    ########
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, head
        # 1 distance apart initially, l = dummy, r = head
        for i in range(1, n):
            head = head.next
        r = head # r always sync with head.  Move head forward. Move l, r forward in the mean time too
        if head:
            head = head.next
            while head:
                l, r = l.next, r.next
                head = head.next

        # r points the last node, l points the to n+1 node from the end
        l.next = l.next.next # bypass n node from the end

        return dummy.next