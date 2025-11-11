
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #####
    # 82. Remove Duplicates from Sorted List II
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description
    #####
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            clean_res = False
            while curr.next and curr.val == curr.next.val:
                # [1,2,3,3,4,4,5] becomes [1,2,5].  The following always remove the current
                # It will remove all continuous duplicates but leave the last duplicate at the current positon
                # Need to remove the residual current instead of moving the cursor.
                prev.next, curr = curr.next, curr.next
                clean_res = True
            if clean_res:
                prev.next, curr = curr.next, curr.next
            else:
                prev, curr = curr, curr.next
        return dummy.next