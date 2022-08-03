'''
test_polymatrix_mult.py
Author: Iskandar Shoyusupov
Date: 7/31/2022
Description: Testing time differences with multithreading and without
             Looking if there is a significant difference

             in progress
'''

import numpy as np
import time
import random
import threading
import os
from numba import jit
import multiprocessing as mp
def rand_c_matrix(size):
    rand_M = np.zeros(size, dtype = int) #Initializing matrix

    for i in range(0,size):
        rand_M[i] = random.randint(0,10)
    return rand_M
#@jit
def no_thread_mult(mat_1,mat_2):
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

    return result 

def upper_calc(diagonal_loc,matrix,store):
    dimension = (diagonal_loc * 2) -1
    result = np.zeros(dimension,dtype = int)

    for i in range(0,diagonal_loc):
        for j in range(0,i + 1):
            result[i] += matrix[i - j,j]
    store.append(result)

def lower_calc(diagonal_loc, matrix,store):
    dimension = (diagonal_loc * 2) -1
    result = np.zeros(dimension,dtype = int)
    
    for i in range(0,diagonal_loc - 1):
        for j in range(0,diagonal_loc - i - 1):
            result[diagonal_loc + i] += matrix[diagonal_loc - j - 1, j + 1 + i]
    store.append(result)

'''
dimension = 5000

a = random_c_matrix_creator(dimension).reshape(1,dimension)
b = random_c_matrix_creator(dimension).reshape(dimension,1)
c = np.matmul(b,a)
'''

'''
Multithreading in Python is not well established and actually made the
program slower. For now will go along with non multi threaded solution


print("MULTITHREADING___________________")
start_time = time.time()

store = []
t1 = threading.Thread(target=upper_calc,args=(dimension,c, store), name="t1")
t2 = threading.Thread(target=lower_calc,args=(dimension,c, store), name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
result = store[0] + store[1]
'''

'''
print("NON MULTI THREADING__________________________")
start_time2 = time.time()
non_thread_reuslt = no_thread_mult(b,a)
print("Matrix mult took " , time.time() - start_time2, "seconds")
'''

