import numpy as np
#Reikna fylki
u = np.array([5,2])
v = np.array([1,3])
A = np.array([[2,3],[4,5]])
B = np.array([[-4,3],[0,1]])
print('i',2*u + 3*v)
print('ii',(np.dot(A,B.T)+((1)/(A+B))*(u+v)))
print('iii', (np.linalg.det(B)+np.dot(u,v)-np.dot(A**5,u)))

def unknowns(a,b):
    return np.linalg.solve(a,b)
A = np.array([[2,-3,1],[1,1,0],[1,0,-2]])
b = np.array([-1,-1,7])
#Remember to move the constants over the other side  
print('Solving 3 variables 3 equations',unknowns(A,b))

#
