import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        
        for (int[] cord : points) {
            int dist = cord[0] * cord[0] + cord[1] * cord[1];
            if (heap.size() < k) {
                heap.offer(new int[]{dist, cord[0], cord[1]});
            } else {
                if (dist < heap.peek()[0]) {
                    heap.poll();
                    heap.offer(new int[]{dist, cord[0], cord[1]});
                }
            }
        }
        
        int[][] result = new int[k][2];
        int idx = 0;
        while (!heap.isEmpty()) {
            int[] point = heap.poll();
            result[idx][0] = point[1];
            result[idx][1] = point[2];
            idx++;
        }
        return result;
    }
}

