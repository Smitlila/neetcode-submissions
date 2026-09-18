class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        r = len(matrix)
        c = len(matrix[0])

        #set the list for the rows and columns with 0 to get the index of the 0 in the main matrix
        row = [0 for _ in range(r)]
        col = [0 for _ in range(c)]


        #will update the row and col when we find 0 
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = -1
                    col[j] = -1
        
        # will update the entire the row and col of the main metrix if their values are not 0
        for i in range(r):
            for j in range(c):
                if row[i] != 0 or col[j] != 0:
                    matrix[i][j] = 0
