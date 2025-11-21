from typing import List
class Solution:
    ######
    # 79. Word Search
    # https://leetcode.com/problems/word-search/description/
    # a backtracking example
    ######
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        # That's edge case that we cannot find any offset within the boundary.
        if m == 1 and n == 1:
            return board[0][0] == word

        def backtrack(pos, idx):
            i, j = pos
            if idx == w:
                return True
            # need if 0 <= r < m and 0 <= c < n to protect index out of range
            if board[i][j] != word[idx]:
                return False
            # supposed you look for
            # CABCEF
            # PXAED
            # XXXC
            # not
            # Supposed you look for ABCEC, we won't find the real solution PX'ABC'EC if we don't backtrack 'E' in ABCEF.
            # That's why we need that backtrack saving and revert
            char = board[i][j]
            board[i][j] = '#'
            for r_off, c_off in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                r, c = i + r_off, j + c_off
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r, c), idx+1):
                        return True
            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack((i, j), 0):
                    return True
        return False