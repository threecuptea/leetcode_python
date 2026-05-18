from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def separate_one_num(num):
            digits = []
            to_process = num
            while to_process > 0:
                digits.append(to_process % 10)
                to_process = to_process // 10

            return digits[::-1]
        result = []
        for num in nums:
            result.extend(separate_one_num(num))

        return result