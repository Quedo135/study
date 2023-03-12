import numpy as np
inf = 10**10

def gcd(a, b):
    while a > 0:
        if b%a:
            a, b = b%a, a
        else:
            return a

def min_price(coins):
    coins.sort()
    a = coins
    n = a[0]
    k = len(coins)
    
    divider = coins[0]
    for i in range(1, k):
        divider = gcd(divider, coins[i])


    if coins[0] == 1:
        return 1
    elif divider > 1:
        return -1
    elif k == 2:
        return coins[0]*coins[1] - coins[0] - coins[1] + 1
    
    visited = [True] + [False]*(n-1)
    Q = [0]
    P = [0] + [inf]*(n-1)
    L = {i:False for i in range(n)}
    L[0] = True
    count = 0
    mod = [c%a[0] for c in a]
    
    while count < n:
        v = Q.pop(0)
        for j in range(1, k):
            u = (v + mod[j])%a[0]
            if visited[u]:
                pass
            P[u] = min(P[u], P[v] + a[j])
            if not L[u]:
                Q.append(u)
                L[u] = True
            
            i = len(Q)
            while i > 1 and P[Q[i-1]] < P[Q[i-2]]:
                Q[i-1], Q[i-2] = Q[i-2], Q[i-1]
                i -= 1
            print(P)
            print(Q)
        visited[v] = True
        count += 1
    return max(P) - a[0] + 1
                
            


    
coins = [6,9,20]

print('result =', min_price(coins))


# 62115
# [103, 194, 387, 615, 881]

# 156140
# [220, 782, 844, 891, 971]

# 196546
# [386, 543, 558, 573, 973]

# 150474
# [208, 640, 719, 783, 809]