
from typing import List
class Solution:
    ######
    # 739. Daily Temperatures
    # https://leetcode.com/problems/daily-temperatures/description/
    ######
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        answers = [0] * n
        stk = []
        # Inspired by Greg Hogg's https://www.youtube.com/watch?v=_ZEvmycwXHs
        # The monotonic stack records those elements haven't got the answer yet and they
        # are in descending order (If it encounters something bigger, it has already pop out.
        # Compare the incoming with the last element, if the incoming element is bigger, pop and record the answer.
        # Since elements are in monotonic descending order, it can continuously process
        # efficiently until it encounter something bigger in the stack
        for i, t in enumerate(temp):
            # found temp greater than before
            while stk and t > stk[-1][0]:
                stk_t, stk_i = stk.pop()
                answers[stk_i] = i - stk_i
            stk.append((t, i))

        return answers