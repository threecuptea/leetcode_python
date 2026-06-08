# https://leetcode.com/problems/maximum-subarray
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prev, max_sum = nums[0], nums[0]
        for i in range(1, n):
            curr = nums[i] if prev < 0 else prev + nums[i]
            max_sum = max(max_sum, curr)
            prev = curr
        return max_sum
    @staticmethod
    def get_test_parameters():
        return [
            {'nums':  [-2,1,-3,4,-1,2,1,-5,4], 'expected': 6},
            {'nums':  [1], 'expected': 1},
            {'nums':  [5,4,-1,7,8], 'expected': 23},
        ]
    def test_subarray_sum(self):
        for testdata in Solution.get_test_parameters():
            assert  self.maxSubArray(testdata['nums']) == testdata['expected']

def main():
    sol = Solution()
    sol.test_subarray_sum()

if __name__ == '__main__':
    main()

