from collections import Counter
with open('input14.txt') as f:
    lines = f.readlines()


def make_input(seq):
    empty_line = seq.index('\n')
    initial = seq[:empty_line]
    initial = initial[0].strip()
    
    formula = seq[empty_line+1:]
    map_entries = {}
    
    for form in formula:
        mapping = form.strip()
        mapping = mapping.split(" -> ")
        map_entries[mapping[0]] = mapping[1]
    return initial, map_entries


def solve_one(initial, maps):

    for _ in range(40):
        next_initial = ""
        for i in range(1, len(initial)):
            pair = f'{initial[i-1]}{initial[i]}'
            mid = maps[pair]
            if next_initial == "":
                next_initial += f'{initial[i-1]}{mid}{initial[i]}'
            else:
                next_initial += f'{mid}{initial[i]}'
        initial = next_initial
    counts = Counter(next_initial).values()
    return max(counts) - min(counts)


inputs = make_input(lines)
initial = inputs[0]
maps = inputs[1]
print(initial)

print(solve_one(initial, maps))