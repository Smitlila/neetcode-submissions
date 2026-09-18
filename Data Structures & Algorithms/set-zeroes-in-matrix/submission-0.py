class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])

        row = [0 for _ in range(r)]
        col = [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = -1
                    col[j] = -1
        
        for i in range(r):
            for j in range(c):
                if row[i] != 0 or col[j] != 0:
                    matrix[i][j] = 0
                    