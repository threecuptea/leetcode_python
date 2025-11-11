from collections import OrderedDict
class LRUCache:
    ################
    # 146. LRU Cache
    # https://leetcode.com/problems/lru-cache/description/
    # The 1st implementation of LRUCache which is backed by double linked list
    # Te 2nd  implementation does not require additional double linked list and is inspired by
    # https://jellis18.github.io/post/2021-11-25-lru-cache/.  It's use OrderedDict which
    # has move_to_end (without deleting first) and popitem(last=False) for FIFO and popitem for LIFO
    ###############
    def __init__(self, capacity: int):
        self.__cache: OrderedDict[int, int] = OrderedDict()
        self.__cap = capacity

    def get(self, key: int) -> int:
        if key not in self.__cache:
            return -1
        self.__cache.move_to_end(key)
        return self.__cache[key]

    def put(self, key: int, value: int) -> None:
        self.__cache[key] = value
        self.__cache.move_to_end(key)
        # Cannot move this to the top of put and check == because new put can be just a replacement.
        # We will remove key prematurely and unnecessarily in that case.
        if len(self.__cache) > self.__cap:
            self.__cache.popitem(last=False)