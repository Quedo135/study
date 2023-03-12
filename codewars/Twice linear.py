import math

def dbl_linear(n):
    nums = set()
    nums.add(1)
    last_added = set()
    last_added.add(1)
    while len(nums) <= n:
        temp = []
        for m in last_added:
            temp.append(2*m + 1)
            temp.append(3*m + 1)
        last_added = set(temp)
        print(sorted(list(last_added)))
        nums.update(last_added)

    return sorted(list(nums))[n]