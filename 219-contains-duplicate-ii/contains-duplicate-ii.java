import java.util.*;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> dist = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (dist.containsKey(nums[i])) {
                if (Math.abs(dist.get(nums[i]) - i) <= k) {
                    return true;
                }
            }
            dist.put(nums[i], i);
        }
        return false;
    }
}

