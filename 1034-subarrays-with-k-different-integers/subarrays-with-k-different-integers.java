import java.util.*;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
    
    private int atMost(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        int left = 0;
        int result = 0;
        
        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];
            if (count.getOrDefault(num, 0) == 0) {
                k--;
            }
            count.put(num, count.getOrDefault(num, 0) + 1);
            
            while (k < 0) {
                count.put(nums[left], count.get(nums[left]) - 1);
                if (count.get(nums[left]) == 0) {
                    k++;
                }
                left++;
            }
            
            result += right - left + 1;
        }
        return result;
    }
}

