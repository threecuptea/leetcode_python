from typing import List
from collections import deque
class Solution:
    ######
    # 200. Number of Islands
    # https://leetcode.com/problems/number-of-islands/description/
    ######
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0
        visited = set()
        dq = deque()
        # This perform much better than 'visit' BFS solution on both CPU and memory
        # This is inspired by Greg Hogg's youtube video https://www.youtube.com/watch?v=gCswsDauXPc
        def bfs():
            while dq:
                i, j = dq.popleft()
                visited.add((i, j))
                for r_off, c_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = i + r_off, j + c_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == '1' and (r, c) not in visited:
                        dq.append((r, c))

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    dq.clear()
                    dq.append((r, c))
                    bfs()


        return islands
    # Time: (m * n)
    # Space: (m * n)

def main():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f'Input= {grid}')
    solution = Solution()
    output = solution.numIslands(grid)
    print(f'Output= {output}')

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f'Input= {grid}')
    output = solution.numIslands(grid)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()
