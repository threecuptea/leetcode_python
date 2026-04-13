# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/place-n-cameras-no-conflict-blocked-grid/problem
# basically it's n-queen problem.  It definitively should not be an easy-level question
# Given an NxN grid where 0 is empty and 1 is blocked, return true if N cameras can be placed
# on empty cells such that no two share the same row, column, or diagonal.
def canPlaceSecurityCameras(N, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    # Write your code here
    def backtrack(row_idx, cameras_placed):
        # Able to place cameras in all rows
        if row_idx == num_rows:
            return True
        # # no two share the same row, column, or "diagonal".
        cols_conflict = []
        for r, c in cameras_placed:
            # add the column of column conflict
            cols_conflict.append(c)
            diff = row_idx - r
            # add columns of "diagonal" conflict.  If the row is two row down, then the column cannot be two column left or right
            cols_conflict.extend([qc for qc in [c - diff, c + diff] if qc >= 0 and qc < num_cols])
        cols_avail = \
            [col_idx for col_idx, val in enumerate(grid[row_idx]) if val == 0 and col_idx not in cols_conflict]
        if not cols_avail:
            return False
        for col in cols_avail:
            cameras_placed.append([row_idx, col])
            # The path work all the way
            if backtrack(row_idx + 1, cameras_placed):
                return True
            # This path does not work
            cameras_placed.pop()

    if backtrack(row_idx = 0, cameras_placed=[]):
        return True
    return False