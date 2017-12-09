# https://leetcode.com/problems/unique-paths/description/
# http://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
# O(mn)

def hello(m,n):
    # Create a 2D table to store
    # results of subproblems
    count=np.zeros((m,n),dtype=int)
    # Count of paths to reach any
    # cell in first column is 1
    for i in range(m):
            count[i][0] = 1
    for j in range(n):
            count[0][j] = 1

            # Calculate count of paths for other
            # cells in bottom-up
            # manner using the recursive solution
    for i in range(1, m):
            for j in range(n):
                count[i][j] = count[i-1][j] + count[i][j-1]
    print(count)
    return count[m-1][n-1]

m=3
n=3
import numpy as np
print(hello(m,n))