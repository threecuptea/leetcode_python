# https://leetcode.com/problems/count-subarrays-with-majority-element-i/description/
from typing import List
class Solution:
    # We enumerate all possible left endpoints i of subarrays and then extend the right endpoint j one position at a time.
    # During this process, we maintain a counter cnt.  If nums[j]=target, we increment cnt by 1; otherwise, we decrement it by 1.
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            if nums[i] == target:
                cnt += 1
            else:
                cnt -= 1
            if cnt > 0:
                ans += 1
            for j in range(i + 1, n):
                if nums[j] == target:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt > 0:
                    ans += 1
        return ans