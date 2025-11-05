from typing import List
import math
class Solution:
    #####
    # 238. Product of Array Except Self
    # https://leetcode.com/problems/product-of-array-except-self/description/
    #####
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        # use math.prod to save loop
        prod_all = math.prod(nums)
        for i, num in enumerate(nums):
            if num == 0:
                prods.append(math.prod(nums[:i]+nums[i+1:]))
            else:
                prods.append(prod_all // num)

        return prods

def main():
    nums = [1,2,3,4]
    print(f'Input= {nums}')
    solution = Solution()
    output = solution.productExceptSelf(nums)
    print(f'Output= {output}')

    nums = [-1,1,0,-3,3]
    print(f'Input= {nums}')
    output = solution.productExceptSelf(nums)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()