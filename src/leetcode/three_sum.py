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
        nums.sort()
        # [-4,-1,-1,0,1,2]
        result = []
        for i in range(len(nums)-2):
            # to avoid duplicate pairs added, process -1 then -1 again
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # the smallest numbers cannot be > 0
            if nums[i] > 0:
                break
            # fix i and let l = i+1, r = len(num)-1, increment l and decrement r
            l, r = i+1,len(nums)-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # To avoid duplicate pair, need l < r to prevent index out of range
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1

        return result


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