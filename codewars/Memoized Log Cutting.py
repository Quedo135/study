def cut_log(p, n):
    k = len(p)
    F = [0] * (n+1)
    for i in range(1, n+1):
        F[i] = max(p[j] + F[i-j] for j in range(i+1))
        print(F)
    return F[n]
    

p = [  0,   1,   5,   8,   9,  10,  17,  17,  20,  24, # 0X's
      30,  32,  35,  39,  43,  43,  45,  49,  50,  54, # 1X's
      57,  60,  65,  68,  70,  74,  80,  81,  84,  85, # 2X's
      87,  91,  95,  99, 101, 104, 107, 112, 115, 116, # 3X's
     119]


print(cut_log(p, 8))




