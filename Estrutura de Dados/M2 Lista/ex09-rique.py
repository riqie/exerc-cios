'''
9. Do fragmento de código abaixo, determine a complexidade:

for i=0 to n-1:                   --> n 
    for j=0 to n-1:               --> n
        mat[i][j] = 0             --> 1
        for k=0 to n-1:           --> n
            mat[i][j] += A[i][k] * B[k][j]  ---> 1

'''

# complexidade = n . n . n 
# complexidade = n³
# complexidade = O(n³) + 2
