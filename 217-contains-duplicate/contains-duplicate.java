import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> dist = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (dist.containsKey(nums[i])) {
                return true;
            }
            dist.put(nums[i], i);
        }
        return false;
    }
}

