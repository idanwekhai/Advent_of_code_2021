import numpy as np
from collections import defaultdict

with open('input.txt') as f:
    all_input = [line for line in f]

fst_row = all_input[0]
nums_to_draw = map(int, fst_row.strip('\n').split(","))
#nos_to_draw = [i for i in nos_to_draw]

matrices_input = all_input[1:]
matrices_input = list(filter(lambda a: a != '\n', matrices_input)) #remove new line character
cleaned_input = [matrices_input[i].strip('\n') for i in range(len(matrices_input))]

def make_matrices(lst, size=5):
  temp = []
  matrix_collect = []
  for i in lst:
    h = map(int, i.strip(" ").split())
    to_int = [i for i in h]
    if len(temp) < size:
      temp.append(to_int)
    else:
      matrix_collect.append(temp)
      temp = []
      temp.append(to_int)
  matrix_collect.append(temp)
  return matrix_collect

def check_win(idx):
  func_temp = np.zeros((5,5), dtype='i')

  if len(idx) == 0:
    return False
    
  for i in idx:
    func_temp[i[0], i[1]] = 1
  for j in func_temp:
    if sum(j) == 5:
      return True
  for k in func_temp.T:
    if sum(k) == 5:
      return True
  return False
 
def mark(drawn, seq):
    idx = np.where(seq==drawn)
    if len(idx[0]) > 0:
      return [int(idx[0]), int(idx[1])]
    return []

def play_game_1(draws_to_take, matrices):
  track = defaultdict(list)
  print(track)

  for pick in draws_to_take:
    for i in range(len(matrices)):
      mat_to_arr = np.array(matrices[i])
    
      idx = mark(pick, mat_to_arr)
      if len(idx) != 0:
        track[i].append(idx)
        is_win = check_win(track[i])
        if is_win:
          return pick, track[i], matrices[i]
  return "End"

def play_game_2(draws_to_take, matrices):
  track = defaultdict(list)
  og_matrix = matrices.copy()

  wins = 0
  win_track = defaultdict(list)
  for pick in draws_to_take:
    for i in range(len(matrices)):
      mat_to_arr = np.array(matrices[i])
    
      idx = mark(pick, mat_to_arr)
      if len(idx) != 0:
        track[i].append(idx)
        is_win = check_win(track[i])
        if is_win:
            if i not in win_track:
                wins += 1
                win_track[i] = track[i]
      if wins == len(matrices):
          return pick, track[i], matrices[i]

def calc_ans(to_draw, matrix, function_name):
    params = function_name(to_draw, matrix)
    number = params[0]
    idxs = params[1]
    print(params)
    print(number)
    mat = np.array(params[2])
    for i in params[1]:
        mat[i[0], i[1]] = 0
    new_mat_sum = sum(sum(mat))
    return number * new_mat_sum

c_matrices = make_matrices(cleaned_input)


#print(calc_ans(nums_to_draw, c_matrices, play_game_1))
print(calc_ans(nums_to_draw, c_matrices, play_game_2))