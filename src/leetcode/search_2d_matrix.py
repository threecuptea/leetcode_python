from typing import List
class Solution:
    ######
    # 981. Time Based Key-Value Store
    # https://leetcode.com/problems/time-based-key-value-store/description/
    ######
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        mat = []
        # one-dimension array
        for i in range(m):
            for j in range(n):
                mat.append(matrix[i][j])

        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            if mat[mid] == target:
                return True
            if target < mat[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
