def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[len(a)//2]
    L = []
    M = []
    R = []
    for x in a:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    print(barrier, a, L, M, R)
    for i,x in enumerate(L + M + R):
        a[i] = x

aa = [1,2,6,2,4,657,3,2,54,89,7]
print(aa)
hoar_sort(aa)
print(aa)
