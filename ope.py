#some basic operations on  matrices
import numpy as np
a=np.array(input('enter the first matrix:'))
b=np.array(input('enter the second matrix:'))
print('the first matrix is a=',a)
print('the second matrix is b=',b)
print('size of a matrix a:',np.shape(a))
print('size of a matrix b:',np.shape(b))
print('determinant of a matrix:',np.linalg.det(a))
print('inverse of a matrix:',np.linalg.inv(a))
print(' addition of matrixes a and b are:',np.add(a,b))
print(' subtraction of  matrices a and b are:',np.subtract(a,b))
print('multiplication of elements in the matrices:',np.multiply(a,b) )
print('matrix multiplication:',np.matmul(a,b))
print('transpose of a matrix:',np.transpose(b))
print('rank of a matrix:',np.linalg.matrix_rank(b))
print('eigen values of a matrix:',np.linalg.eig(b))
print(' maximums of the matrices :',np.maximum(a,b))
print('upper triangular matrix of a matrix:',np.triu(a))
print('lower triangular matrix of a matrix:',np.tril(b))
