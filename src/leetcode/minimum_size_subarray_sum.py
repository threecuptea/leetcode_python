from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        total = 0
        # instead of sum(arr...) which repeat the same and the calculation is very time consuming.
        # Use total increment and decrement one value  to cut down running time.  That makes a difference
        # In sliding window, we often use normal range for r.  It will advance any way
        # Let l to shrink as needed.  Longest Substring Without Repeating Characters is another sliding window example
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r -l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
