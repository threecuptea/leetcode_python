
class Solution:
    # ######
    # 12. Integer to Roman
    # https://leetcode.com/problems/integer-to-roman/description/
    ########
    def intToRoman(self, num: int) -> str:
        single_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        double_dict = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
        res = num
        # This will return both the residual after subtracting the number and return roman characters
        def advance(res, d):
            for n, ro in d.items():
                if res >= n:
                    # This step will move III in one shot and make it more efficient
                    times = res // n
                    return (res - n * times, ro * times)
        res = num
        ch_arr = []
        while res > 0:
            if str(res)[0] in ['4', '9']:
                w_dict = double_dict
            else:
                w_dict = single_dict
            res, chars = advance(res, w_dict)
            ch_arr.append(chars)

        return ''.join(ch_arr)


def main():
    num = 3749
    solution = Solution()
    output = solution.intToRoman(num)
    print(f'Output= {output}')

    num = 58
    output = solution.intToRoman(num)
    print(f'Output= {output}')

    num = 1994
    output = solution.intToRoman(num)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()