# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/reverse-even-indexed-nodes/problem
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def extractAndAppendSponsoredNodes(head):
    # Write your code here
    # Zero or one node
    if not head or not head.next:
        return head
    # it is reverse, we might not to single out
    if not head.next.next:
        new_head = head.next
        new_head.next, head.next = head, None
        return new_head
    # head = [10, 20, 30, 40, 50, 60]
    # [20, 40, 60, 50, 30, 10]
    idx = 0
    dummy = SinglyLinkedListNode(-999999)
    dummy.next = head
    odd_prev, even_prev, curr = dummy, head, head
    while curr:
        if idx >= 1:
            if idx % 2 == 1:
                odd_prev.next = curr
                odd_prev = curr
                curr = curr.next
            else: # even case
                nxt = curr.next
                curr.next = even_prev
                even_prev = curr
                curr = nxt
        else:
            curr = curr.next
        idx += 1
    odd_prev.next = even_prev
    head.next = None
    return dummy.next