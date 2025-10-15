class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        temp = [[0 for _ in range(len(matrix))]for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            #print(matrix[i])
            for x in range(len(matrix[0])):
                temp[x][i]=matrix[i][x]
        return temp