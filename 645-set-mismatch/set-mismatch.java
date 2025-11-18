import java.util.*;

class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int a = 0, b = 0;
        
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            a += num;
            set.add(num);
        }
        for (int num : set) {
            b += num;
        }
        
        int s = n * (n + 1) / 2;
        
        return new int[]{a - b, s - b};
    }
}

