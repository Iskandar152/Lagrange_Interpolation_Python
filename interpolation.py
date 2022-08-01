'''
Author: Iskandar Shoyusupov
Date: 7/31/2022
'''
import numpy as np
import time

cmatrix_1 = np.matrix([1,2,3,4,5,6,7,8,9,10]) #Test coefficient matrix 1 
cmatrix_2 = np.matrix([[10],[9],[8],[7],[6],[5],[4],[3],[2],[1]])  #Test coefficient matrix 2 
def multiply(mat_1, mat_2):
    product = np.matmul(mat_1,mat_2)         #Product of the two coefficient matrices
    diagonal_loc = product.shape[0]          #Steps to diagonal
    dimension = (diagonal_loc * 2) -1        #Dimension of the vector space
    result = np.zeros(dimension,dtype = int) #Result array
    
    for i in range(0,diagonal_loc):
        for j in range(0,i + 1):
            result[i] += product[i - j,j]
    for i in range(0,diagonal_loc - 1):
        for j in range(0,diagonal_loc - i - 1):
            result[diagonal_loc + i] += product[diagonal_loc - j - 1, j + 1 + i]
    print("Multiplying\n",mat_1)
    print("By\n", mat_2)
    print("Equaling:")
    print(product)
    print('-----------------')
    print("result coefficient matrix:")
    print(result)

start_time = time.time()

multiply(cmatrix_2,cmatrix_1)

print("Matrix mult took " , time.time() - start_time, "seconds")
