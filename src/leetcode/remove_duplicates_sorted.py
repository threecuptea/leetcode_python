from typing import List
class Solution:
    ########
    # Remove duplicates from sorted array
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    #######
    def removeDuplicates(self, nums: List[int]) -> int:
        # Read numbers backward so that no need to re-organize orders. It ends with 1
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    output = solution.removeDuplicates(nums)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()