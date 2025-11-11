from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #####
    # 206. Reverse Linked List
    # https://leetcode.com/problems/reverse-linked-list/description/
    #####
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # Reverse always start with the prev None or nil
        prev, curr = None, head
        while curr:
            nxt = curr.next # IMPORTANT: keep the next before reassign the prev to the next for reversal
            curr.next = prev
            prev, curr = curr, nxt
        return prev