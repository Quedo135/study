def solve_runes(runes):
    runes_mod = runes.replace('=-', '+')
    runes_mod = runes_mod.replace('=', '-')
    runes_mod = runes_mod.replace('*-', '*(-1)*')
    runes_mod = runes_mod.replace('--', '+')
    
    for d in '123456789':
        txt = runes_mod.replace('?', d)
        if eval(txt) == 0:
            return int(d)
    for i in range(len(runes_mod)):
        if runes_mod[i] =='?':
            if i == 0:
                runes_mod = runes_mod[1:]
            elif runes_mod[i-1] not in '+-*':
                
        
        
        elif ('?0' in runes or '??' in runes ) and d == '0' or d in runes:
            continue
    return -1

a = '?878+-663-?2?5'
eval(a)


