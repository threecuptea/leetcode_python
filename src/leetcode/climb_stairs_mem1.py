class Solution:
    ######
    # 70. Climbing Stairs
    # https://leetcode.com/problems/climbing-stairs/description/
    # The same as fibonacci sequence
    #
    ######
    # inspired by Greg Hogg's https://www.youtube.com/watch?v=I-R1XsECJu8
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev, curr = 1, 2
        for i in range(2, n):
            prev, curr = curr, prev + curr
        return curr