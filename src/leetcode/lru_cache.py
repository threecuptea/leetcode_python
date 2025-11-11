

class ListNode:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
################
# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/
# The 1st implementation of LRUCache which is backed by double linked list
# LRUCache has left and right pointer.  The left's next points to the least used node
# the right's prev point points to the most recent ued node.  Always append at the end
################
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # key pointing to ListNode
        self.cap = capacity
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        # insert between self.right and self.right.prev
        self.right.prev.next, node.prev = node, self.right.prev
        node.next, self.right.prev = self.right, node

    def remove(self, node):
        # remember to include both directions.
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            # re-organization
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            self.remove(node)
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)