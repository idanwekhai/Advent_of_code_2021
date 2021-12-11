import numpy as np
with open('input9.txt') as f:
    rows = f.readlines()

def make_input(seq):
    master_list = []
    for line in seq:
        lst = [int(i) for i in line.strip("\n")]
        master_list.append(lst)
    return np.array(master_list)

def get_low_points(arr):
  shape = arr.shape
  cols = shape[1]
  rows = shape[0]
  ren = []
  for i in range(rows):
    for j in range(cols):
      if i == 0:
        if j == 0:
          adj = [arr[i,j+1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        elif j == cols-1:
          adj = [arr[i, j-1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        else:
          adj = [arr[i,j-1], arr[i+1,j], arr[i,j+1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
      elif i == rows-1:
        if j == 0:
          adj = [arr[i-1,j], arr[i,j+1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        elif j == cols-1:
          adj = [arr[i-1,j], arr[i,j-1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        else:
          adj = [arr[i,j-1], arr[i-1,j], arr[i,j+1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
      elif j == 0:
        if i == 0:
          adj = [arr[i,j+1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        elif i == cols-1:
          adj = [arr[i-1,j], arr[i,j+1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        else:
          adj = [arr[i-1,j], arr[i,j+1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
      elif j == cols-1:
        if i == 0:
          adj = [arr[i,j-1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        elif i == rows-1:
          adj = [arr[i-1,j], arr[i,j-1]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
        else:
          adj = [arr[i-1,j], arr[i,j-1], arr[i+1,j]]
          if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
      else:
        adj = [arr[i,j-1], arr[i-1,j], arr[i+1,j], arr[i,j+1]]
        if arr[i,j] < min(adj): ren.append(arr[i,j]+1)
  return sum(ren)


#print(make_input(rows))
print(get_low_points(make_input(rows)))