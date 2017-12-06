# Zero Matrix: Write an algorithm such that if an element
# in an MxN matrix is 0, its entire row and column are set to 0.
# Logic - note down i,j that is row an column locations in an array. Later convert the matrix to numpy matrix and rewrite
ip=[[1,1,1,0],[1,0,1,1],[1,1,1,1]]
import numpy as np

array=[]
for i,each in enumerate(ip):
    for j,every in enumerate(each):
        if every==0:
            array.append([i,j])
print(array)
ip=np.matrix(ip)
for tt in array:
    ip[tt[0],:]=0
    ip[:,tt[1]]=0
print(ip)
