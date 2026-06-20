# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description
import copy
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        if head.next and head.next.next is None:
            return head.val + head.next.val
        def reverseList(hd: ListNode) -> ListNode:
            prev, curr = None, hd
            while curr:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            return prev

        def fold(hd: ListNode) -> (ListNode, ListNode):
            dummy = ListNode(0, hd)
            l, lp, r, rp = hd, dummy, hd, dummy
            while r.next:
                lp, l = l, l.next
                if r.next:
                    rp, r = rp.next, r.next
                    if r.next:
                        rp, r = rp.next, r.next
            # 5  4  2  1
            #    lp l
            # lp: the end of 1st half, l: the beginning of 2nd half
            # fold, 1st half reverse, the 2nd half remains. 4 5
            #                                               2 1
            lp.next = None # cut the half
            rev = reverseList(copy.deepcopy(hd))
            return rev, l

        f, s = fold(head)
        f_prev, f_curr, s_prev, s_curr = None, f, None, s
        result = 0
        while f_curr:
            result = max(result, f_curr.val + s_curr.val)
            f_prev, f_curr, s_prev, s_curr = f_curr, f_curr.next, s_curr, s_curr.next

        return result