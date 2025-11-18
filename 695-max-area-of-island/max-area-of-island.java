class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int maxArea = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j, m, n, 0);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
    
    private int dfs(int[][] grid, int i, int j, int m, int n, int area) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1) {
            return area;
        }
        grid[i][j] = 0;
        area += 1;
        area = dfs(grid, i, j + 1, m, n, area);
        area = dfs(grid, i + 1, j, m, n, area);
        area = dfs(grid, i, j - 1, m, n, area);
        area = dfs(grid, i - 1, j, m, n, area);
        return area;
    }
}

