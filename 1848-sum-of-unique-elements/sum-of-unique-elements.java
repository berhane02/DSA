import java.util.ArrayList;
class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer, Integer> index = new HashMap<>();
        int sum = 0;
        for(int n: nums){
            if (index.containsKey(n)){
                index.put(n, index.get(n)+1);
            }else {
                index.put(n,1);
            }
        
        }

        
        for (int key : index.keySet()){

            if(index.get(key) == 1){
                sum += key;
            }
        }
        return sum;
        
        
    }
}