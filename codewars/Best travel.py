def choose_best_sum(s, n, v):
    Q = [(0, len(v), 0)]                # stack of points - (sum way length, possible cities, current step)
    while Q and Q[0][2] < n:            # checking if Q is not empty and number of steps is less then n
        p, m_index, count = Q.pop(0)    
        for i in range(m_index):
            if p+v[i] <= s:             # if the sum is less or equal s, add point to the stack
                Q.append((p + v[i], i, count + 1)) 
    
    return max(a[0] for a in Q if a[0] <= s and a[2] == n) if Q else None 
            


    # k = len(a)
    # a.sort()
    # print(a)
    # if n == 1:
    #     if a[0] < s:
    #         for i in range(1, k):
    #             if a[i] > s: 
    #                 return a[i-1]
    #             elif a[i] == s: return s
    #     else:
    #         return None
    # res = [0] * (k+1)
    # for j in range(k):
    #     b = choose_best_sum(s - a[j], n-1, a[:j] + a[j+1:])
    #     res[j] = a[j] + b if b else 0
    #     print(res[j], a[j])
    # return max(filter(lambda x: x <= s, res)) or None
    
v = [340, 500, 640, 732, 890, 1000, 1230, 1230, 1320, 1346, 1440, 2333]
s = 2300
n = 4
print(choose_best_sum(s, n, v))