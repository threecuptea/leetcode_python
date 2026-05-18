from typing import List
class Solution:
    #####
    # 219. Contains Duplicate II
    # https://leetcode.com/problems/contains-duplicate-ii/description/
    #####
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        val_idx = {}
        for i, num in enumerate(nums):
            if num not in val_idx:
                val_idx[num] = i
            else:
                if i - val_idx[num] <= k:
                    return True
                else:
                    val_idx[num] = i

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