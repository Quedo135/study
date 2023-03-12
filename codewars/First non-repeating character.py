def first_non_repeating_letter(string):
    for m in string:
        if string.lower().count(m.lower()) == 1:
            return m
        
a = 'sTress'

print(first_non_repeating_letter(a))