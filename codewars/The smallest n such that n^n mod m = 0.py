from math import sqrt
from functools import reduce 

def f(m:int) -> int:
    factors = dict()
    primes = [2, 3, 5, 7, 11, 13, 17]
    for p in primes:
        while m%p == 0:
            m //= p
            factors[p] = factors.get(p, 0) + 1
    f = primes[-1] + 2
    while m > 1:
        if all(f%p != 0 for p in primes):
            primes.append(f)
            while m%f == 0:
                m //= f
                factors[f] = factors.get(f, 0) + 1
        f += 2
    
    def prod(v):
        res = 1
        for i in range(k):
            res *= used_primes[i]**v[i]
        return res
    def satisfy(v, n):
        return all(v[i]*n >= factors[used_primes[i]] for i in range(k))
    
    
    used_primes = list(factors.keys())

    k = len(used_primes)
    v = [1]*k
    n = prod(v)    
    if satisfy(v,n):
        return n
    
    Q = [[1]*k]         # starting vertex
    max_index = [k]     # max index of corr vertex from Q
    R = []
    while Q:
        v = Q.pop(0)
        l = max_index.pop(0)
        for growing_prime in range(l):
            v[growing_prime] += 1
            n = prod(v)
            if satisfy(v, n):
                R.append(prod(v))
            else:
                Q.append(v)
                max_index.append(growing_prime)
            print(Q)
            print(R)
            v[growing_prime] -= 1
    return min(R)
        
            
# not necessary to up the power of the primes
# it is possible to multiply the primes by any other number!!!!

    
m = 243
print(f(m))
a,b = 1234567890, 411522630
