import numpy as np

with open('input.txt') as f:
    all_input = [line for line in f]

def make_input(seq):
    all_lines = []
    for line in seq:
        line = line.strip('\n').split(" -> ")
        cleaned = [list(map(int, i.split(","))) for i in line]
        all_lines.append(cleaned)
    return np.array(all_lines)

def points_between_straight(x1, y1, x2, y2):
    d0 = x2 - x1
    d1 = y2 - y1  
    count = max(abs(d1+1), abs(d0+1))
    if d0 == 0:
        if d1 > 0:
            ys = np.arange(y1, y2+1).tolist()
        else:
            ys = np.arange(y1, y2-1,-1).tolist()
        xs  = [x1] * int(abs(d1)+1)
        return [i for i in zip(xs, ys)]
    if d1 == 0:
        if d0 > 1:
            xs = np.arange(x1, x2+1).tolist()
        else:
            xs = np.arange(x1, x2-1,-1).tolist()
        ys = [y1] * int(abs(d0)+1)
        return [i for i in zip(xs, ys)]

def points_between_straight_diagonal(x1, y1, x2, y2):
    d0 = x2 - x1
    d1 = y2 - y1

    if d0 == 0:
        if d1 > 0:
            ys = np.arange(y1, y2+1).tolist()
        else:
            ys = np.arange(y1, y2-1,-1).tolist()
        xs  = [x1] * int(abs(d1)+1)
        return [i for i in zip(xs, ys)]

    if d1 == 0:
        if d0 > 1:
            xs = np.arange(x1, x2+1).tolist()
        else:
            xs = np.arange(x1, x2-1,-1).tolist()
        ys = [y1] * int(abs(d0)+1)
        return [i for i in zip(xs, ys)]
        
    if (x1 == y1) and (x2==y2):
        if y2 > y1:
            xs = np.arange(x1, x2+1).tolist()
            ys = np.arange(y1, y2+1).tolist()
        else:
            xs = np.arange(x1, x2-1, -1).tolist()
            ys = np.arange(y1, y2-1, -1).tolist()
        return [i for i in zip(xs, ys)]
        
    if (x1 == y2) and (x2 == y1):
        if d0 < 0:
            xs = np.arange(x1, x2-1,-1).tolist()
            ys = np.arange(y1, y2+1).tolist()
        else:
            xs = np.arange(x1, x2+1).tolist()
            ys = np.arange(y1, y2-1, -1).tolist()
        return [i for i in zip(xs, ys)]
    
    if abs(d1/d0) == 1:
        if d1 == d0 and d1<0:
            xs = np.arange(x1, x2-1, -1).tolist()
            ys = np.arange(y1, y2-1, -1).tolist()
        elif d1 == d0 and d1>0:
            xs = np.arange(x1, x2+1).tolist()
            ys = np.arange(y1, y2+1).tolist()
        else:
            if d0 < 0:
                xs = np.arange(x1, x2-1, -1).tolist()
                ys = np.arange(y1, y2+1).tolist()
            else:
                xs = np.arange(x1, x2+1).tolist()
                ys = np.arange(y1, y2-1, -1).tolist()
                
        return [i for i in zip(xs, ys)]

def solve1(seq):
    grid = np.zeros((1000, 1000))
    for c in seq:
        if (c[0,0] == c[1,0]) or (c[0,1] == c[1,1]):
          coords_between = points_between_straight(c[0,0], c[0,1], c[1,0], c[1,1])
          for i in coords_between:
            grid[i[1]][i[0]] += 1
    answer = len(np.where(grid>1)[0])
    return answer

def solve2(seq):
    grid = np.zeros((1000, 1000))
    for c in seq:
        coords_between = points_between_straight_diagonal(c[0,0], c[0,1], c[1,0], c[1,1])
        for i in coords_between:
          grid[i[1]][i[0]] += 1
    answer = len(np.where(grid>1)[0])
    return answer

all_coordinates = make_input(all_input)
Ans1 = solve1(all_coordinates)
Ans2 = solve2(all_coordinates)
print(Ans1)
print(Ans2)