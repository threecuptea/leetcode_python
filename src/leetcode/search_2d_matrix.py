from typing import List
class Solution:
    ######
    # 981. Time Based Key-Value Store
    # https://leetcode.com/problems/time-based-key-value-store/description/
    ######
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            if target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
        return False
