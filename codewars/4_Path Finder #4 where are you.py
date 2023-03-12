dx,dy = -1, 0   # initial movement direction
x, y = 0, 0     # initial position

def i_am_here(path):
    global x, y, dx, dy     # need to store in global vars to save between function calls
    com = [m for m in path]
    i = 1
    while i < len(com):         # divide path to separate instructions
        if com[i].isdecimal() and com[i-1].isdecimal(): # if two adjacent parts are numbers - glue them
            com[i-1] = com[i-1] + com[i]    
            com.pop(i)
        else: i += 1
    for instr in com:
        if instr == 'l':        # turning legt
            dx, dy = -dy, dx
        elif instr == 'r':      # turning right
            dx, dy = dy, -dx
        elif instr in 'LR':     # rotation to the opposite direction ( +pi )
            dx, dy = -dx, -dy
        else:                   # move in the current direction for a given number of steps
            x += dx * int(instr) 
            y += dy * int(instr)
    return [x, y]


path = "10r5r0"
print(i_am_here(path))
print(i_am_here(path))
print(i_am_here(path))



    
    
    


    
