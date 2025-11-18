import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);
        
        for (int i = 1; i < intervals.length; i++) {
            int[] current = intervals[i];
            int[] last = merged.get(merged.size() - 1);
            
            if (current[0] <= last[1]) {
                merged.set(merged.size() - 1, new int[]{last[0], Math.max(last[1], current[1])});
            } else {
                merged.add(current);
            }
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
}

