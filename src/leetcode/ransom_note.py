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
        # if keys(words) of the counter of ransom is not subset of keys(words) of magazine
        if not c_ran.keys() <= c_mag.keys():
            return False
        for k, v in c_ran.items():
            # Need more than maazine can provide
            if v > c_mag[k]:
                return False
        return True

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