# profrom matrix multiplication and find again value and vector using tensorflow

import tensorflow as tf
print("Name :-Rajan K Tiwari Roll no:- 35 ")
print("Matrix multiplication using tensorflow ")
x=tf.contant([1,2,3,4,5,6],shape=[2,3])
y=tf.contant([7,8,9,10,11,12],shape=[3,2])
print("x=",x)
print("y=",y)
z=tf.matmul(x,y)
print("matrix multipation =",z)

ematrix = tf.random.uniform ([2,2],minval=3,maxval=10,dtype=tf.float32,name="matrix A")
print("Matrix A =\n\n".format(ematrix))
evalue,evactore=tf.linalg.eight(ematrix)
print("eigen vector: {}/n/n Eigen vector:{}m/n ".format(evalue,evactore))




