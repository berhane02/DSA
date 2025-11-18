import java.util.*;

class Solution {
    private Map<String, Integer> memo = new HashMap<>();
    
    public int longestPalindromeSubseq(String s) {
        return dp(0, s.length() - 1, s);
    }
    
    private int dp(int left, int right, String s) {
        if (left > right) {
            return 0;
        }
        if (left == right) {
            return 1;
        }
        
        String key = left + "," + right;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        int result;
        if (s.charAt(left) == s.charAt(right)) {
            result = dp(left + 1, right - 1, s) + 2;
        } else {
            result = Math.max(dp(left, right - 1, s), dp(left + 1, right, s));
        }
        
        memo.put(key, result);
        return result;
    }
}

