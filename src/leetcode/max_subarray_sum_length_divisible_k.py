from typing import List
class Solution:
    #######
    # 3381. Maximum Subarray Sum With Length Divisible by K
    # https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/
    #######
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        p_sum = [0] * (len(nums) + 1) # prefix sum
        m_sum = [float('-inf')] * (len(nums) + 1)
        # [-5,1,2,-3,4], k = 2
        # m_sum[-inf, -inf, -4, 3, -1, 4], 4 = 1 + 2 + -3 + 4 (include 4 instead of 2 numbers )
        for i, num in enumerate(nums):
            # 1-base index
            p_sum[i + 1] = p_sum[i] + num
            if i + 1 >= k:
                # the baseline, the sum of the last size k
                m_sum[i + 1] = p_sum[i + 1] - p_sum[i + 1 -k]
                if m_sum[i + 1 -k] > 0:
                    m_sum[i + 1] += m_sum[i + 1 -k]

        return max(m_sum)