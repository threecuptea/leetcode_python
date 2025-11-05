
class Solution:
    #########
    # 13. Roman to Integer
    # https://leetcode.com/problems/roman-to-integer/description/
    # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    #
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    #########
    def romanToInt(self, s: str) -> int:
        single_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        double_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        # No need to x 10 since it represents 10
        while i < len(s):
            if i+2 <= len(s) and s[i:i+2] in double_dict:
                num += double_dict[s[i:i+2]]
                i += 2
            else:
                num += single_dict[s[i]]
                i += 1
        return num

def main():
    s = "III"
    solution = Solution()
    output = solution.romanToInt(s)
    print(f'Output= {output}')

    s = "LVIII"
    output = solution.romanToInt(s)
    print(f'Output= {output}')

    s = "MCMXCIV"
    output = solution.romanToInt(s)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()