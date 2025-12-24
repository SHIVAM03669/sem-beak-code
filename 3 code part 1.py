# 1329. Sort the Matrix Diagonally
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

# Example 1:


# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# Example 2:

# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

def diagonalSort(mat):
    m = len(mat)
    n = len(mat[0])

    #function to sort one diaogonal

    def sort_diagonal(r,c):
        i,j = r,c
        diagonal = []

        #collecting diagonal elememnt
        while i < m and j < n:
            diagonal.append(mat[i][j])
            i+= 1
            j +=1
        #sort diagonal
        diagonal.sort()

        #put back sorted value
        i,j = r,c
        idx = 0

        while i<m and j<n:
            mat[i][j] = diagonal[idx]
            idx += 1
            i +=1
            j+=1
    
    #start from  first column
    for row in range(m):
        sort_diagonal(row,0)
    
    #start from top row (skip first column)
    for col in range(1,n):
        sort_diagonal(0, col)

    return mat