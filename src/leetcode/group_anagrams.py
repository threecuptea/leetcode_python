from typing import List
from collections import defaultdict
class Solution:
    ####
    # 49. Group Anagrams
    # https://leetcode.com/problems/group-anagrams/description/
    #####
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = defaultdict(list)
        for s in strs:
            # "eat","tea","ate" will all use "aet" as the key to group
            dict_map[''.join(sorted(s))].append(s)

        return [v for _, v in dict_map.items()]

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f'Input= {strs}')
    solution = Solution()
    output = solution.groupAnagrams(strs)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()