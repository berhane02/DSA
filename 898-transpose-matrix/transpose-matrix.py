class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        res = []
        for i in range(len(matrix[0])):
            temp = []
            for x in range(len(matrix)):
                temp.append(matrix[x][i])
            res.append(temp)
        return res