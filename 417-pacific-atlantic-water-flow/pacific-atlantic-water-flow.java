import java.util.*;

class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        
        Queue<int[]> pQ = new LinkedList<>();
        Set<String> pSeen = new HashSet<>();
        Queue<int[]> aQ = new LinkedList<>();
        Set<String> aSeen = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            pQ.offer(new int[]{0, i});
            pSeen.add(0 + "," + i);
        }
        for (int i = 1; i < m; i++) {
            pQ.offer(new int[]{i, 0});
            pSeen.add(i + ",0");
        }
        
        for (int i = 0; i < m; i++) {
            aQ.offer(new int[]{i, n - 1});
            aSeen.add(i + "," + (n - 1));
        }
        for (int i = 0; i < n - 1; i++) {
            aQ.offer(new int[]{m - 1, i});
            aSeen.add((m - 1) + "," + i);
        }
        
        Set<String> pCord = getCord(pQ, pSeen, heights, m, n);
        Set<String> aCord = getCord(aQ, aSeen, heights, m, n);
        
        List<List<Integer>> result = new ArrayList<>();
        for (String cord : pCord) {
            if (aCord.contains(cord)) {
                String[] parts = cord.split(",");
                result.add(Arrays.asList(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])));
            }
        }
        return result;
    }
    
    private Set<String> getCord(Queue<int[]> q, Set<String> seen, int[][] heights, int m, int n) {
        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int i = curr[0], j = curr[1];
            seen.add(i + "," + j);
            
            for (int[] dir : directions) {
                int r = i + dir[0], c = j + dir[1];
                String key = r + "," + c;
                if (r >= 0 && r < m && c >= 0 && c < n && 
                    heights[r][c] >= heights[i][j] && !seen.contains(key)) {
                    seen.add(key);
                    q.offer(new int[]{r, c});
                }
            }
        }
        return seen;
    }
}

