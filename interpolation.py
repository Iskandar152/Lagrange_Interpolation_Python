import numpy as np

cmatrix_1 = np.matrix([1,2,3,4,5,6,7])
cmatrix_2 = np.matrix([[7],[6],[5],[4],[3],[2],[1]])
def multiply(mat_1, mat_2):
    product = np.matmul(mat_1,mat_2)         #Product of the two coefficient matrices
    diagonal_loc = product.shape[0]          #Steps to diagonal
    dimension = (diagonal_loc * 2) -1        #Dimension of the vector space
    result = np.zeros(dimension,dtype = int) #Result array
    
    for i in range(0,diagonal_loc):
        for j in range(0,i + 1):
            result[i] += product[i - j,j]
    for i in range (0,dimension,):
        print(i)

    print(dimension)
    print("Multiplying\n",mat_1)
    print("By\n", mat_2)
    print("Equaling:")
    print(product)
    print('-----------------')
    print(result)
    
multiply(cmatrix_2,cmatrix_1)
