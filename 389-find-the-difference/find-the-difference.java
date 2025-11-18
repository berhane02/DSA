class Solution {
    public char findTheDifference(String s, String t) {
        int c = 0;
        for (char cs : s.toCharArray()) {
            c ^= cs;
        }
        for (char ct : t.toCharArray()) {
            c ^= ct;
        }
        return (char) c;
    }
}

