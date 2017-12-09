# https://leetcode.com/problems/merge-intervals/solution/
# O(nlgn)

def hello(m,n):
    count=np.zeros((m,n),dtype=int)
    for i in range(m):
            count[i][0] = 1
    for j in range(n):
            count[0][j] = 1
    for i in range(1, m):
            for j in range(n):
                count[i][j] = count[i-1][j] + count[i][j-1]
    print(count)
    return count[m-1][n-1]

m=3
n=3
import numpy as np
print(hello(m,n))
