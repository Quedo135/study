import numpy as np

def gcd(a, b):
    while a > 0:
        if b%a:
            a, b = b%a, a
        else:
            return a

def min_price(coins):
    k = len(coins)
    coins.sort()

    common_divider = coins[0]
    s = []
    for c in coins[1:]:
        common_divider = gcd(common_divider, c)    
        s.append(c * coins[0] // gcd(c, coins[0]))
    
    print(*s, sep = '\n')

    if common_divider != 1:
        return -1    
    elif coins[0] == 1:
        return 1


    if k == 2:
        return coins[0]*coins[1] - coins[0] - coins[1] + 1

    n = max(c * (c%coins[0] + 1) for c in coins[1:])
    # n = min(s)
    print('N=', n)

    F = np.zeros((n+1,k+1), dtype=int)
    F[0,:] = 1
    
    last_zero = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            F[i,j] = F[i,j-1] if coins[j-1]>i else F[i-coins[j-1],j] + F[i,j-1]
        if F[i,k] == 0:
            last_zero = i
        elif i - last_zero >= coins[1]:
            return last_zero + 1
    return -1        

coins = [49,15,24]

print('result =', min_price(coins))


# 62115
# [103, 194, 387, 615, 881]

# 156140
# [220, 782, 844, 891, 971]

# 196546
# [386, 543, 558, 573, 973]

# 150474
# [208, 640, 719, 783, 809]