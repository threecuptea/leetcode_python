from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        tmp = head
        # To avoid the complication k can be > n and we count node and get a clean/ net k
        while tmp:
            n += 1
            tmp = tmp.next
        k = k % n
        if k == 0:
            return head
        dummy = ListNode(0, head)
        l, r = dummy, head
        # Initially has 1 distance apart
        for i in range(1, k):
            head = head.next
        r = head
        if head:
            head = head.next
            while head:
                l, r = l.next, r.next
                head = head.next
        # the r points to the last node, l points to the node of k distance to the left
        r.next = dummy.next
        dummy.next = l.next
        l.next = None
        return dummy.next
