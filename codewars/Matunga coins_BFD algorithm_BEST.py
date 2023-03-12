def gcd(a, b):
    while a > 0:
        if b%a:
            a, b = b%a, a
        else:
            return a

def min_price(coins):
    """ Using BFD algorithm for the Frobenius number """

    a = sorted(coins) 
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
    
    Q = [0]                         # queue of vertixes, which was 'seen' before 
    P = [k-1] + [0]*(n-1)           # max index of step, which we should examine when standing on vertix
    mod = [c%a[0] for c in a]       # in fact, the lenght of step
    S = [0] + [a[0]*a[-1]]*(n-1)    # current path weight of each vertex
    L = [1] + [0]*(n-1)             # flag of vertex presence in Q
    
    while Q:
        v = Q.pop(0)                # getting FIFO vertex from queue
        L[v] = 0        
        for j in range(1, P[v]+1):  # examining the outbound edges from v 
            u = (v + mod[j])%a[0]   
            if S[u] > S[v] + a[j]:  
                S[u] = S[v] + a[j]  # if current path is longer, change it
                P[u] = j            # and set the max step to scan from vertex equals j
                if not L[u]:        
                    Q.append(u)     # adding vertex to queue if it is not currently there
                    L[u] = 1
            
    return max(S) - a[0] + 1

        
        
    
            


    
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