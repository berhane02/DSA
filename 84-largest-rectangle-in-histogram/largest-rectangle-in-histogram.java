import java.util.*;

class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int area = 0;
        Stack<int[]> stk = new Stack<>();
        
        for (int i = 0; i < heights.length; i++) {
            int height = heights[i];
            int start = i;
            
            while (!stk.isEmpty() && height < stk.peek()[0]) {
                int[] top = stk.pop();
                int h = top[0], j = top[1];
                int w = i - j;
                area = Math.max(area, h * w);
                start = j;
            }
            stk.push(new int[]{height, start});
        }
        
        while (!stk.isEmpty()) {
            int[] top = stk.pop();
            int h = top[0], j = top[1];
            area = Math.max(area, h * (n - j));
        }
        
        return area;
    }
}

