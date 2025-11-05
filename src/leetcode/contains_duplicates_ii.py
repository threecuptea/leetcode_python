from collections import Counter
from typing import List
class Solution:
    #####
    # 219. Contains Duplicate II
    # https://leetcode.com/problems/contains-duplicate-ii/description/
    #####
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        keys = {k for k, v in counter.items() if v > 1}
        if len(keys) == 0:
            return False
        # This tries to get around huge size of list w/o duplicates
        # It's a shortcut to only check keys of duplicates
        for key in keys:
            starting = 0
            while starting < len(nums)-1:
                try:
                    idx = nums.index(key, starting)
                except ValueError:
                    break
                try:
                    nums.index(key, idx+1, idx+k+1)
                    return True
                except ValueError:
                    starting = idx + 1
        return False

def main():
    nums = [1, 2, 3, 1]
    k = 3
    print(f'Input= {nums}, {k}')
    solution = Solution()
    output = solution.containsNearbyDuplicate(nums, k)
    print(f'Output= {output}')

    nums = [1, 0, 1, 1]
    k = 1
    print(f'Input= {nums}, {k}')
    solution = Solution()
    output = solution.containsNearbyDuplicate(nums, k)
    print(f'Output= {output}')

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(f'Input= {nums}, {k}')
    solution = Solution()
    output = solution.containsNearbyDuplicate(nums, k)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()