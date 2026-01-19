from typing import List
#####
# 15, 3Sum
# https://leetcode.com/problems/3sum/description/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
######
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We need to sort to avoid duplicate pairs added to result
        nums.sort()  # to avoid duplicates and maintain the natural order
        result = set()
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    # list is mutable and cannot be hashed.  Need to use tuple
                    result.add((nums[i], nums[l], nums[r]))
                    l, r = l + 1, r - 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return [list(tup) for tup in list(result)]


def main():
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    output = solution.threeSum(nums)
    print(f'Output= {output}')

    nums = [0,1,1]
    output = solution.threeSum(nums)
    print(f'Output= {output}')

    nums = [0,0,0]
    output = solution.threeSum(nums)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()