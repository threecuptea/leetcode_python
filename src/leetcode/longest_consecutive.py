from typing import List
class Solution:
    ######
    # 128. Longest Consecutive Sequence
    # https://leetcode.com/problems/longest-consecutive-sequence/
    ######
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0
        for val in st:
            # Find the starting point val
            if val-1 in st:
                continue
            cnt = 1
            curr = val
            while (curr+1) in st:
                curr, cnt = curr+1, cnt + 1
            longest = max(longest, cnt)

        return longest

def main():
    nums = [100,4,200,1,3,2]
    print(f'Input= {nums}')
    solution = Solution()
    output = solution.longestConsecutive(nums)
    print(f'Output= {output}')

    nums = [0,3,7,2,5,8,4,6,0,1]
    print(f'Input= {nums}')
    output = solution.longestConsecutive(nums)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()