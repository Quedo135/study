import numpy as np


def exp_sum(n):
    F = np.zeros((n+1, n+1), dtype=int)
    F[0,:] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            F[i,j] = F[i, j-1] if j>i else F[i-j,j] + F[i, j-1]
    print(F)
    return F[n,n]
    
n = 3
print(exp_sum(n))