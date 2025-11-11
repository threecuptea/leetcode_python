from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #####
    # 21. Merge Two Sorted Lists
    # https://leetcode.com/problems/merge-two-sorted-lists/description/
    # spicing together with those two list instead creating new nodes
    #####
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        dummy = ListNode(0)
        prev = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next, list1 = list1, list1.next
            else:
                prev.next, list2 = list2, list2.next
            prev = prev.next
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return dummy.next