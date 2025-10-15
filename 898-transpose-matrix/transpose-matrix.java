class Solution {
    public int[][] transpose(int[][] matrix) {
        
        int[][] result = new int[matrix[0].length][matrix.length];
        for(int i =0; i<matrix.length; i++){
            for (int x =0; x<matrix[0].length; x++){
                result [x][i] = matrix[i][x];
            }
        }
        return result;
    }
}