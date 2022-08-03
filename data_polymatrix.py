import test_polymatrix_mult as poly
from matplotlib import pyplot as plt
import numpy as np
import time
dimensions = np.zeros(500, dtype = int)
times = np.zeros(500, dtype = float)
dimension_size = 1
for i in range(0,500):
    mat1 = poly.rand_c_matrix(dimension_size).reshape(1,dimension_size)
    mat2 = poly.rand_c_matrix(dimension_size).reshape(dimension_size,1)
    prod_mat12 = np.matmul(mat2,mat1)

    start_time = time.time()
    result = poly.no_thread_mult(mat2,mat1)
    final_time = time.time()-start_time

    dimensions[i] = dimension_size
    times[i] = final_time
    dimension_size += 1

print(times)
print(dimensions)

plt.plot(dimensions,times)
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.savefig("Result_Coefficient.png",bbox_inches='tight')
plt.show()

