from typing import List

class Solution:
    # 1. Two Sum
    # https://leetcode.com/problems/two-sum/description/
    # Given an array of integers nums and an integer target, return indices of the two numbers
    # such that they add up to target.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        # This is efficient because it build the hashmap to lookup and look up specifically by compliment
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map:
                return [num_map[compliment], i]
            num_map[num] = i
        return []

def main():
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    output = solution.twoSum(nums, target)
    print(f'Output= {output}')

    nums = [3,2,4]
    target = 6
    output = solution.twoSum(nums, target)
    print(f'Output= {output}')

    nums = [3,3]
    target = 6
    output = solution.twoSum(nums, target)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()