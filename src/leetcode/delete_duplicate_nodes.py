# from HackRank
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/remove-consecutive-duplicates-sorted-list/problem
#
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteDuplicates(head):
    if not head:
        return None
    # Write your code here
    dummy = SinglyLinkedListNode(-999999)
    dummy.next = head
    prev, curr = dummy, head
    # It needs curr not curr.next so that it will compare the last node (it might have duplicate value)
    while curr:
        if curr.data == prev.data:
            nxt = curr.next
            prev.next, curr = nxt, nxt
        else:
            prev, curr = curr, curr.next

    return dummy.next

