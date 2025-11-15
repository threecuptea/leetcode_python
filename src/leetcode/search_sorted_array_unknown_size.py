# class ArrayReader:
# def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        l, r = 0, 2
        # It turns out that returns 2**31 - 1 if the i is out of the boundary of the array is not a factor
        while reader.get(r-1) < target:
            l = r
            r <<= 1
        r -= 1
        while l <= r:
            mid = l + ( r - l) // 2
            got = reader.get(mid)
            if got == target:
                return mid
            if target > got:
                l = mid + 1
            else:
                r = mid - 1

        return -1
