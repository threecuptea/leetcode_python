# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/one-pass-removal-kth-from-end/problem
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def removeKthNodeFromEnd(head, k):
    # Write your code here
    dummy = SinglyLinkedListNode(-1)
    dummy.next = head
    lp, r = dummy, head # left prev, r will point to the last one.
    # if n = 2, lp and r should have 2 distance apart.
    remove_beyond = False
    for _ in range(k):
        if r.next:
            r = r.next
        else:
            remove_beyond = True
            break
    if remove_beyond:
        return head
    while r.next:
        lp, r = lp.next, r.next
    target = lp.next
    lp.next = target.next

    return dummy.next