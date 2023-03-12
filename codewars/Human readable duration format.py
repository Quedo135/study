def format_duration(seconds):
    if seconds == 0:
        return 'now'
    y = seconds // 31536000
    d = (seconds % 31536000) // 86400
    h = (seconds % 86400) // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 60)
    
    res = ''
    if y > 0:
        lat = (d>0) + (h>0) + (m>0) + (s>0)
        res += f'{y} year' + 's'*(y>1) + ', '*(lat>1) + ' and '*(lat==1)
    if d > 0:
        lat = (h>0) + (m>0) + (s>0)
        res += f'{d} day'*(d>0) + 's'*(d>1) + ', '*(lat>1) + ' and '*(lat==1)
    if h > 0:
        lat = (m>0) + (s>0)
        res += f'{h} hour' * (h>0) + 's'*(h>1) + ', '*(lat>1) + ' and '*(lat==1)
    if m > 0:
        res += f'{m} minute'*(m>0) + 's'*(m>1) + ' and '*(s>0)
    if s > 0:  
        res += f'{s} second' * (s>0) + 's'*(s>1)
    return res


a = 3662
print(format_duration(a))