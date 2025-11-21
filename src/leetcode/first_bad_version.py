
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r-l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        # it would stop when l = r
        if isBadVersion(l):
            return l
        return -1