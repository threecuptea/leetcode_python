from collections import Counter

class Solution:
    ####
    # 217. Contains Duplicate
    # https://leetcode.com/problems/contains-duplicate/description
    #####
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return any(val > 1 for val in counter.values())

def main():
    nums = [1,2,3,1]
    print(f'Input= {nums}')
    solution = Solution()
    output = solution.containsDuplicate(nums)
    print(f'Output= {output}')

    nums = [1,2,3,4]
    print(f'Input= {nums}')
    solution = Solution()
    output = solution.containsDuplicate(nums)
    print(f'Output= {output}')

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(f'Input= {nums}')
    solution = Solution()
    output = solution.containsDuplicate(nums)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()