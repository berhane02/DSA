class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> unix = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            if (unix.containsKey(target-nums[i])){

                return new int[]{unix.get(target-nums[i]), i};
            }
            unix.put(nums[i],i);

        }
        throw new IllegalArgumentException("No two sum solution");
    }
}