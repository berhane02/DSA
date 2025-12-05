class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while top <= bottom and left <= right:
            # left -> right along top
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # top -> bottom along right
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # right -> left along bottom (if still valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # bottom -> top along left (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res