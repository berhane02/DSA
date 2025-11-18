class Solution {
    public int findMinMoves(int[] machines) {
        int sumM = 0;
        for (int m : machines) {
            sumM += m;
        }
        
        if (sumM % machines.length != 0) {
            return -1;
        }
        
        int res = 0;
        int avg = sumM / machines.length;
        int runningMachine = 0;
        
        for (int n : machines) {
            int numMov = n - avg;
            runningMachine += numMov;
            res = Math.max(res, Math.max(Math.abs(runningMachine), numMov));
        }
        return res;
    }
}

