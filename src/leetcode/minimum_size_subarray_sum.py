from typing import List
class Solution:
    ######
    # 209. Minimum Size Subarray Sum
    # https://leetcode.com/problems/minimum-size-subarray-sum/description/
    ######
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float('inf')
        total = 0
        # instead of sum(arr...) which repeat the same and calculation is time consuming.
        # Use total increment and decrement to cut down running time.  That makes a difference
        # In sliding window, we often use normal range for r.  It will advance any way
        # Let l to shrink as needed
        for r in range(len(nums)):
            total += nums[r]
            # need to use 'while' instead of if, otherwise the length stay the same because of l-1, r+1
            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len


