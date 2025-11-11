
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #####
    # 25. Reverse Nodes in k-Group
    # https://leetcode.com/problems/reverse-nodes-in-k-group/description/
    #####
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, tmp, lp = head, head, dummy
        while curr:
            hr = curr # keep partial/ residual head
            partial = False
            # we read ahead to ensure that we are not reverse partial list
            for i in range(k):
                if not tmp.next and i < k -1:
                    partial = True
                    break
                tmp = tmp.next
            if partial:
                lp.next = hr
                break
            # lp always points to the connecting node prior to the next reverse list.
            prev, new_lp = None, curr  # prev left
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            # prev points the right, curr points to the following
            lp.next = prev
            lp =  new_lp

        return dummy.next
