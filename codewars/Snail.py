import numpy as np

def snail(s):
    k = len(s[0])
    n = len(s)
    print(s)
    if n == 2:
        return s[0] + s[1][::-1]
    elif n == 1:
        return s[0]
    res = s[0] + [s[j][-1] for j in range(1, n)] + s[-1][-2::-1] + [s[-j][0] for j in range(2, n)]
    res += snail([s[j][1:-1] for j in range(1, n-1)])
    return res
