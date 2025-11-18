import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        for (int[] prereq : prerequisites) {
            int a = prereq[0], b = prereq[1];
            g.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
        }
        
        int notvisited = 0, visiting = 1, visited = 2;
        int[] status = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, g, status, notvisited, visiting, visited)) {
                return false;
            }
        }
        return true;
    }
    
    private boolean dfs(int i, Map<Integer, List<Integer>> g, int[] status, 
                       int notvisited, int visiting, int visited) {
        if (status[i] == visiting) return false;
        if (status[i] == visited) return true;
        
        status[i] = visiting;
        
        List<Integer> neighbors = g.getOrDefault(i, new ArrayList<>());
        for (int n : neighbors) {
            if (!dfs(n, g, status, notvisited, visiting, visited)) {
                return false;
            }
        }
        status[i] = visited;
        return true;
    }
}

