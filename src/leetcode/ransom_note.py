from collections import Counter
class Solution:
    ######
    # 383, Ransom note
    ## https://leetcode.com/problems/ransom-note/description/
    ########
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter is very handy here
        c_ran = Counter(ransomNote)
        c_mag = Counter(magazine)
        return all(k in c_mag and c_mag[k] >= c for k, c in c_ran.items())

def main():
    ransom_note, magazine = "a", "b"
    solution = Solution()
    output = solution.canConstruct(ransom_note, magazine)
    print(f'Output= {output}')

    ransom_note, magazine = "aa", "ab"
    output = solution.canConstruct(ransom_note, magazine)
    print(f'Output= {output}')

    ransom_note, magazine = "aa", "aab"
    output = solution.canConstruct(ransom_note, magazine)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()