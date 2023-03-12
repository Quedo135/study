def match(s):
    d = {'A':'B', 'B':'A', 'X':'Y', 'Y':'X'}
    
    if len(s) < 2:
        return 0
    # elif len(s) == 2:
    #     return 1 if s[0] == s[1] else 0
    
    res = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == d[s[j]]:
                res = max(res, 1 + match(s[:i] + s[j+1:]))
    print(s, res)      
    return res



s = "AAAABBBB"

print(match(s))
