import numpy as np
def gcd(a, b):
    a, b = min(a,b), max(a,b)
    while a > 1:
        if b%a:
            a, b = b%a, a
        else:
            return a
    return 1        

def lcm(a,b):
    return a*b//gcd(a,b)

def survivor(z):
    return lcm(z[0],z[1]) + lcm(z[0],z[2]) - sum(z)

z, r =[687,829,998],45664

print(survivor(z))
          
print((6*9*20)**0.5*8/3.1415)