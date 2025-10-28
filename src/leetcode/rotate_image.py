from typing import List
# python -m leetcode.rotate_image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # This should be square: n * n
        n = len(matrix)
        # Starting the outer later, move the value to the right and downward clockwise
        # shrink top, right, bottom, and left once finish one layer until top >= bottom
        top, right, bottom, left = 0, n-1, n-1, 0
        while True:
            # boundary need to set dynamically by left and right since it will shrink after we finish one layer
            # Need to exclude right; otherwise the corner number like 1 would be moved to the position of 3 then
            # the position of 9 repeatedly
            for i in range(left, right):
                # in clockwise, m[top][i] -> m[i][right], m[i][right] -> m[bottom][n-1-i]
                # m[bottom][n-1-i]-> m[n-1-i][left], m[n-1-i][left] -> m[top][i], that finish the cycle
                # 1 -> 3, 3-> 9, 9 -> 7, 7 -> 1; 2 -> 6, 6 -> 8, 8 -> 4, 4 ->2
                # I re-use restore and kept variable to keep memory usage low.
                restore = matrix[top][i]
                kept = matrix[i][right]
                matrix[i][right] = restore

                # bottom would be moved right to left relatively. The formula should be adjust accordingly
                restore = kept
                kept = matrix[bottom][n-1-i]
                matrix[bottom][n-1-i] = restore

                restore = kept
                kept = matrix[n-1-i][left]
                matrix[n-1-i][left] = restore

                restore = kept
                matrix[top][i] = restore
            # Advance to the inner layer
            top, right, bottom, left = top+1, right-1, bottom -1, left+1
            if top >= bottom:
                break

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(f'Input= {matrix}')
    solution = Solution()
    solution.rotate(matrix)
    print(f'Output= {matrix}')

if __name__ == "__main__":
    main()