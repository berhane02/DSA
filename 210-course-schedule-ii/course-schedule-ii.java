import java.util.*;

class Solution {
    private List<Integer> res = new ArrayList<>();
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        for (int[] prereq : prerequisites) {
            int a = prereq[0], b = prereq[1];
            g.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
        }
        
        int notvisited = 0, visiting = 1, visited = 2;
        int[] status = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, g, status, notvisited, visiting, visited)) {
                return new int[0];
            }
        }
        
        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }
        return result;
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
        res.add(i);
        return true;
    }
}

