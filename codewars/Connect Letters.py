def match(s):
    d = {'A':'B', 'B':'A', 'X':'Y', 'Y':'X'}
    n = len(s)
    
    # constructing the function of maximum number of connections in sequence from symbol j to symbol i (inclusive)
    # first index is finish and the second - start
    # border conditions: F[i, j] = 0 for all j >= i
    
    F = [[0]*n for i in range(n)]       

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if s[j] == d[s[i]]:                                             # check if border sybols are equal
                F[i][j] = 1 + F[i-1][j+1]                                   # and return F of the sequence without them + 1
            elif i-j > 2:                                                   # check if sum of parts of splitted sequenсe gives better result
                F[i][j] = max(F[k][j] + F[i][k+1] for k in range(j, i-1))   # it is possible if the number of symbols > 3
            F[i][j] = max(F[i-1][j], F[i][j+1], F[i][j])                    # check shorter sequence: with finish-1 or start+1
    return (F[n-1][0])                                                      # result for the sequence starting at 0 and finishing at n-1


s = "XYABXYXYAB"

print(match(s))
