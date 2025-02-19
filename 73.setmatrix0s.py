matrix = [[1,1,1],[1,0,1],[1,1,1]]

#logic
'''
find the row with a 0 in it, find its position in the matrix as well. 

once row is found, make the entire row 0,0,.., and change the zeroes at that position in the other matrix 

what if there are more zeroes than 1? well have to go search first then change. 
first get position as i and j (i is row and j is column) for each 0 value present, then change accordingly
'''

matrix_zeroes = [] #[[0,0][0,3]]
#searching for 0s -> finding the zeroes' positions
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            matrix_zeroes.append([i,j])
#changing 
'''i need to change column first, and then come to row as the row remains static'''

for i in range(len(matrix_zeroes)): # 0,1
    for j in range(len(matrix_zeroes[i])): #0,1
        pos = matrix_zeroes[i][j] #0->row #0->column
        if j == 0: 
            for k in range(len(matrix[pos])): #[0,1,2,0]
                matrix[pos][k] = 0 #[0,0,0,0]
        else:  #j = 1 -> column 
            for k in matrix: 
                k[pos] = 0 

print(matrix)


            






