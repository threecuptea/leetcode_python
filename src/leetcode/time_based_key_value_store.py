from collections import defaultdict
class TimeMap:
    ######
    # 981. Time Based Key-Value Store
    # https://leetcode.com/problems/time-based-key-value-store/description/
    #
    ######
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps timestamp of set are strictly increasing.
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        # len should be the partial list by key
        l, r = 0, len(values) - 1
        # PLEASE Use plain binary search, don't think too much for now
        while l <= r:
            mid = l + (r-l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
