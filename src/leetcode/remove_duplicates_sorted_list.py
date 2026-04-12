# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/remove-consecutive-duplicates-sorted-list/problem?isFullScreen=true
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# This is a better version and no need to have dummy or prev. However, be cautious of consecutive the same number
def deleteDuplicates(head):
    if not head:
        return None
    # Write your code here
    curr = head
    while curr.next:
        nxt = curr.next
        if nxt.data == curr.data:
            # curr need to remain in the case so that it can compare the nxt.next. There can be consecutive the same number
            # 1,2,2,2,3,4,4,5
            curr.next = nxt.next
        # move on only when curr and next is different
        else:
            curr = curr.next

    return head