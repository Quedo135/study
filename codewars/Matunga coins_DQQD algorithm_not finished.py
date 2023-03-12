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
    n = coins[0]   
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
    
    S = np.full(n, coins[-1])
    S[0] = 0
    P = np.zeros(n, dtype=int)
    P[0] = n
    Q = {0:[0]}
    L = [1]
    Z = [0]
    mod = [c%coins[0] for c in coins]
    
    
    while Z:
        w = Z.pop()
        print('w =', w)
        while len(Q[w]):
            v = Q[w].pop()
            for j in range(1, P[v]):
                u = v + mod[j]
                w = S[v] + coins[j]
                if u >= coins[j]:
                    u -= coins[0]
                    w -= 1
                if w < S[u]:
                    
                    

    
            
            
    
    
coins = [6,7,8]


print('result =', min_price(coins))


# 62115
# [103, 194, 387, 615, 881]

# 156140
# [220, 782, 844, 891, 971]

# 196546
# [386, 543, 558, 573, 973]

# 150474
# [208, 640, 719, 783, 809]