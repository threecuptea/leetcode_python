from typing import List
class Solution:
    ########
    # 11. Container With Most Water
    ########
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            if height[l] < height[r]:
                max_area = max(max_area, height[l] * (r-l))
                l += 1
            else:
                max_area = max(max_area, height[r] * (r-l))
                r -= 1
        return max_area

def main():
    height = [1,8,6,2,5,4,8,3,7]
    print(f'Input= {height}')
    solution = Solution()
    output = solution.maxArea(height)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()
