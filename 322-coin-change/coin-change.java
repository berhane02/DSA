class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] arr = java.util.stream.IntStream.generate(() -> Integer.MAX_VALUE).limit(amount+1).toArray();
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