from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    #####
    # 147. Insertion Sort List
    # https://leetcode.com/problems/insertion-sort-list/description/
    #####
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(-9999, head)
        prev, curr = head, head.next
        while curr:
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue
            tmp = dummy
            while curr.val > tmp.next.val:
                tmp = tmp.next
            prev.next = curr.next # current's next
            curr.next = tmp.next
            tmp.next = curr
            curr = prev.next

        return dummy.next