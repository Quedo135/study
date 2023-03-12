import numpy as np
inf = 10**5                             # can use float('inf'), but int is more useful with numpy arrays

def path_finder(maze):
    N = len(maze.split())
    
    mp = np.array([[m != 'W' for m in line] for line in maze.split()])
    p = np.full((N,N), inf)
    p[0,0] = 0
    seen = set([(0,0)])
    moves = ((0,1), (0,-1), (1,0), (-1,0))

    def legal_moves(x,y):
        return [(x+dx,y+dy) for dx,dy in moves if 0<=x+dx<N and 0<=y+dy<N and mp[x+dx,y+dy]]

    while seen:
        x,y = min(seen, key = lambda x_y: p[x_y])
        if (x,y) == (N-1,N-1): return p[x,y]
        for x1,y1 in legal_moves(x,y):
            p[x1,y1] = min(p[x1,y1], p[x,y] + 1)
            seen.add((x1,y1))
        seen.remove((x,y))
        mp[x,y] = 0
    return False
    

a1 = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

 
print(path_finder(c))




