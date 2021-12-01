with open('input.txt') as f:
    numbers = [int(line) for line in f]


def create_window_sums(lst):
    window_sums = []
    for i in range(len(lst)-2):
        window = lst[i] + lst[i+1] + lst[i+2]
        window_sums.append(window)
    return window_sums


def larger_than_prev(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] != lst[0] and lst[i] > lst[i-1]:
            count += 1
    return count

fst_ans = create_window_sums(numbers)
snd_ans = larger_than_prev(fst_ans)

print(snd_ans)
