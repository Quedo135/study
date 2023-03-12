def sum_strings(x, y):
    x = x.lstrip('0')
    y = y.lstrip('0')
    
    if not x and not y:
        return 0
    
    x = x.zfill(max(len(x), len(y)))[::-1]
    y = y.zfill(max(len(x), len(y)))[::-1]
    
    add = 0
    res = []
    for (a,b) in zip(map(int,x), map(int,y)):
        res.append((a + b + add) % 10)
        add = (a + b + add)//10
    if add:
        res.append(add)
    print(res[::-1])
    return ''.join(str(m) for m in res[::-1])
        

x,y = '0000', '00'


print(sum_strings(x,y))
    # def digit_generator(l):
    #     s, k, n = 0, 0, 0
    #     i = 1
    #     while i <= l:
    #         n = int(x[-i]) if i < lx + 1 else 0
    #         k = int(y[-i]) if i < ly + 1 else 0
    #         yield str((n + k + s) % 10)
    #         s = (n + k + s) // 10
    #         i += 1
    # lx, ly = len(x), len(y)
    # l = max(lx, ly) + 1
    # res = []
    # nums = digit_generator(l)
    # for i in range(l): res.append(str(next(nums)))
    # return ''.join(res[::-1]).lstrip('0')