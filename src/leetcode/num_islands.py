from typing import List
class Solution:
    ######
    # 200. Number of Islands
    # https://leetcode.com/problems/number-of-islands/description/
    ######
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0
        # This perform much better than 'visit' BFS solution on both CPU and memory
        # This is inspired by Greg Hogg's youtube video https://www.youtube.com/watch?v=gCswsDauXPc
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j-1)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i+1, j)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

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

