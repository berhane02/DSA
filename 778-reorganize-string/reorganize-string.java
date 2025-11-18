import java.util.*;

class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        for (Map.Entry<Character, Integer> entry : count.entrySet()) {
            maxHeap.offer(new int[]{entry.getValue(), entry.getKey()});
        }
        
        int[] prev = new int[]{0, 0};
        StringBuilder res = new StringBuilder();
        
        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            int cnt = curr[0];
            char ch = (char) curr[1];
            
            res.append(ch);
            cnt -= 1;
            
            if (prev[0] > 0) {
                maxHeap.offer(prev);
            }
            prev = new int[]{cnt, ch};
        }
        
        return (res.length() == s.length()) ? res.toString() : "";
    }
}

