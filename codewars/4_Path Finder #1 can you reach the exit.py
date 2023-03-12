import numpy as np
inf = 10**5                             # can use float('inf'), but int is more useful with numpy arrays

def path_finder(maze):
    """ We will store all naigbor points wich we see during the path and 

    Args:
        maze (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    N = len(maze.split())
    
    mp = np.array([[m != 'W' for m in line] for line in maze.split()])
    seen = set([(0,0)])
    print(mp)
    moves = ((0,1), (0,-1), (1,0), (-1,0))

    def legal_moves(x,y):
        return [(x+dx,y+dy) for dx,dy in moves if 0<=x+dx<N and 0<=y+dy<N and mp[x+dx,y+dy]]

    while seen:
        (x,y) = seen.pop()
        print('seen',seen ,'x,y ' ,x ,y)
        if (x,y) == (N-1,N-1): return True
        for x1,y1 in legal_moves(x,y):
            seen.add((x1,y1))
            print('seen',seen)
        mp[x,y] = 0
    return False
    
    
    
    
    

a1 = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])

 
print(path_finder(a1))




