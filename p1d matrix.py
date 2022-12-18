# Demonstration of marrix in python
import numpy as np
print("Name :-Rajan K Tiwari Roll no:- 35 ")
m1=np.matrix([1,2,3],[2,3,7],[7,8,9])
m2=np.matrix([1,4,7],[8,5,2],[9,6,3])
print("matrix 1 =",m1)
print("matrix 2 =",m2)
print("shape m1=",m1.shape)
print("shape m2=",m2.shape)
ans1=np.add(m1,m2)
print("matrix Addition = ",ans1)
print("shape of ans1=", ans1.shape)

ans2=np.matmul(m1,m2)
print("matrix multiplye = ",ans2)
print("shape of ans1=", ans2.shape)

ans3=np.transpose(m1)
print(ans3)
ans4=np.transpose(m2)
print(ans4)






