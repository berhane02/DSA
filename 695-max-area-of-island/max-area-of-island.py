class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        max_area=0

        def dfs(i,j, area):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return area
            else:
                grid[i][j] = 0
                area += 1
                area = dfs(i,j+1,area)
                area = dfs(1+i,j,area)
                area = dfs(i,j-1,area)
                area = dfs(i-1,j,area)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j,0)
                    max_area = max(max_area, area)
        return max_area