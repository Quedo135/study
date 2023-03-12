def valid_braces(string):
    d = {')':'(', ']':'[', '}':'{'}
    a = []
    print(d)
    for m in string:
        print(a)
        if m not in '(){}[]':
            continue
        if m in '([{':
            a.append(m)
        else:
            if not a:
                return False
            if d[m] == a[-1]:
                a.pop()
            
    return False if a else True


aa = "{}()[]"

print(valid_braces(aa))