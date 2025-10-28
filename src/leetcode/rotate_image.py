from typing import List
# python -m leetcode.rotate_image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # This should be square: n * n
        n = len(matrix)
        # Starting the outer layer in onion peel way, any position should move bottom - top step
        # shrink top, right, bottom, and left once finidh one later until top >= bottom
        top, right, bottom, left = 0, n-1, n-1, 0
        while True:
            # boundary need to set dynamically since it will shrink after one cycle,
            # Need to avoid right; otherwise the corner number would be moved repeatedly.
            for i in range(left, right):
                # in clockwise, m[top][i] -> m[i][right], m[i][right] -> m[bottom][i]
                # m[bottom][i] -> [i][left], m[i][left] -> m[top][i], that finish the cycle
                # 1 -> 3, 3-> 9, 9 -> 7, 7 -> 1, 2 -> 6, 6 -> 8, 8 -> 4
                restore = matrix[top][i]
                kept = matrix[i][right]
                matrix[i][right] = restore

                # bottom would be moved right to left relatively. The formula should be reversed.
                restore = kept
                kept = matrix[bottom][n-1-i]
                matrix[bottom][n-1-i] = restore

                restore = kept
                kept = matrix[n-1-i][left]
                matrix[n-1-i][left] = restore

                restore = kept
                matrix[top][i] = restore

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