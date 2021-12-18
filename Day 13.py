import numpy as np
with open('input.txt') as f:
    coords = f.readlines()


def make_input(seq):
    empty_line = seq.index('\n')
    coords = seq[:empty_line]
    folds = seq[empty_line+1:]
    
    max_x = 0
    max_y = 0
    
    coords_list = []

    for i in coords:
        coord = i.strip().split(",")
        coord = [int(i) for i in coord]
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
        coords_list.append(coord)
        
    folds_list = []
    
    for j in folds:
        fold = j.strip()
        idx = fold.index("g")
        fold = fold[idx+2:].split("=")
        folds_list.append(fold)
    return coords_list, folds_list, max_x, max_y

def roll_horizontal(arr, y):
    top = arr[:y]
    bottom = arr[y+1:]
    bottom = np.flip(bottom, 0)
    return top + bottom

def roll_vertical(arr, x):
    arr = arr.T
    top = arr[:x]
    bottom = arr[x+1:]
    bottom = np.flip(bottom, 0)
    new_arr = top+bottom
    return new_arr.T
    

def solve_one(coords, folds, maxX, maxY):
    paper = np.zeros((maxY+1, maxX+1))
    emp_after = []
    for idx in coords:
        paper[idx[1], idx[0]] = 1
    for i in folds:
        if i[0] == 'y':
            paper = roll_horizontal(paper, int(i[1]))
            emp_after.append(len(np.where(paper>0)[0]))
        else:
            paper = roll_vertical(paper, int(i[1]))
            emp_after.append(len(np.where(paper>0)[0]))
    print(paper)
    return emp_after
    
def solve_two(coords, folds, maxX, maxY):
    paper = np.zeros((maxY+1, maxX+1))
    emp_after = []
    for idx in coords:
        paper[idx[1], idx[0]] = 1
    for i in folds:
        if i[0] == 'y':
            paper = roll_horizontal(paper, int(i[1]))
            emp_after.append(len(np.where(paper>0)[0]))
        else:
            paper = roll_vertical(paper, int(i[1]))
            emp_after.append(len(np.where(paper>0)[0]))
    paper = paper.astype('int64')
    paper = np.where(paper>0, "#", paper)
    paper = np.where(paper=="0", ".", paper)
    paper = paper.tolist()
    return ["".join(i) for i in paper]


inputs = make_input(coords)

coords = inputs[0]
folds = inputs[1]
max_x = inputs[2]
max_y = inputs[3]



print(solve_one(coords, folds, max_x, max_y))
print(solve_two(coords, folds, max_x, max_y))
