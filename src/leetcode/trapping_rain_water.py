from typing import List
######
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
######
class Solution:
    # The key point is that it will trap water only if the current height is low than surrounding ones;
    # otherwise, the water will overflow (the negative case)
    # the amount of water trap is min(max_l, max_r) - height[i]
    # max_l or max_r should be ones before l or r cursor move. max_l or max_r will be adjusted
    # once it pass the current height
    # It is inspired by neetcode's video https://www.youtube.com/watch?v=ZI2z5pq0TqA
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        max_l, max_r = height[0], height[n-1]
        res = 0
        while l < r:
            if max_l < max_r:
                l += 1
                if max_l - height[l] > 0:
                    res += max_l - height[l]
                max_l = max(max_l, height[l])
            else:
                r -= 1
                if max_r - height[r] > 0:
                    res += max_r - height[r]
                max_r = max(max_r, height[r])
        return res

def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(f'Output= {solution.trap(height)}')

    height = [4,2,0,3,2,5]
    print(f'Output= {solution.trap(height)}')

if __name__ == "__main__":
    main()