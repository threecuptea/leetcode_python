class Solution:
    #####
    # 69. Sqrt(x)
    # https://leetcode.com/problems/sqrtx/description/
    #
    class Solution:
        #####
        # 33. Search in Rotated Sorted Array
        #
        #####
        def mySqrt(self, x: int) -> int:
            if x == 0 or x == 1:
                return x
            l, r = 0, x // 2
            while l <= r:
                m = l + (r -l) // 2
                if m**2 == x:
                    return m
                elif m**2 < x:
                    l = m + 1
                else:
                    r = m - 1
            # the loop break when l = r + 1 and r becomes smaller index. Therefore, we should use r whose r**2 < x
            return r