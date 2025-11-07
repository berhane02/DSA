class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] arr = new int[amount+1];
        Arrays.fill(arr, Integer.MAX_VALUE);
        arr[0] = 0;
        for(int i = 1; i<amount+1; i++){
            for(int c: coins){
                
                if(i-c>=0 && arr[i - c] != Integer.MAX_VALUE){
                    arr[i] = Math.min(arr[i],arr[i-c]+1);
                }
            }
        }
        return arr[amount] != Integer.MAX_VALUE ? arr[amount] : -1;
        
    }
}