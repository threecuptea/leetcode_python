# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # simplify (minutes / 60 - (hour % 12 * 60 + minutes)/(60 * 12)) * 360
        ans = abs(minutes * 6 - (hour % 12  * 60 + minutes) / 2)
        return 360 - ans if ans > 180 else ans