def longest_repetition(txt:str) -> tuple:
    count = 1
    res = (txt[0], 1)
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            count += 1
        else: 
            if res[1] < count:
                res = (txt[i-1], count)
            count = 1
        if i == len(txt)-1 and res[1] < count:
            res =  (txt[i-1], count)
    return res


txt = "bbbaaabaaadaaaaa"
        

print(longest_repetition(txt))    
    
res = ('u', 3)