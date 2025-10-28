from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box_num(r, c):
            return (r // 3) * 3 + c // 3 # r

        row_idx, col_idx, box_idx = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(0, 9):
            for col in range(0, 9):
                val = board[row][col]
                if val.isdigit():
                    box = get_box_num(row, col)
                    if row_idx.get(val) and row in row_idx.get(val):
                        return False
                    if col_idx.get(val) and col in col_idx.get(val):
                        return False
                    if box_idx.get(val) and box in box_idx.get(val):
                        return False
                    row_idx[val].add(row)
                    col_idx[val].add(col)
                    box_idx[val].add(box)
        return True

def main():
    board =[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(f'Input= {board}')
    solution = Solution()
    print(f'Output= {solution.isValidSudoku(board)}')

if __name__ == "__main__":
    main()