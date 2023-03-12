def max_sum_path(l1, l2):
    p0, p1 = [0,0], [0,0]                       # indexes of the last cross and of the current positions for both lists
    s = 0                                       # current sum      
    while p1[0] < len(l1) and p1[1] < len(l2):  
        if l1[p1[0]] == l2[p1[1]]:              # if found equal elements
            s += max(sum(l1[p0[0]: p1[0]]), sum(l2[p0[1]: p1[1]]))  # calc the largest sum since the last cross
            p0 = p1[::]                         # setting the last cross position
            p1[0] += 1                          # move to the next points in both lists        
            p1[1] += 1
        else:
            line = int(l2[p1[1]] < l1[p1[0]])   # select line with smaller current element
            p1[line] += 1                       # and moving forward
    s += max(sum(l1[p0[0]:]), sum(l2[p0[1]:]))  # adding the tail to the sum
    return s

a, b = [2, 3, 7, 10, 12], [1, 5, 7, 8]

max_sum_path(a, b)

