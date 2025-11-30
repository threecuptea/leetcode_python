from typing import List
class Solution:
    #######
    # 3761. Minimum Absolute Distance Between Mirror Pairs
    # https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/
    #######
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def net(n):
            p = n
            while p % 10 == 0:
                p = p // 10
            return p
        d = {}
        m_dist = 999999
        # Need to store net or cleaned num.  However, it is directional, [120, 21] work but [21, 120] does not work
        # Therefore, adding condition.
        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])
            net_num = net(num)
            if rev in d and net_num == num:
                m_dist = min(m_dist, i - d[rev])
            d[net_num] = i

        return -1 if m_dist == 999999 else m_dist