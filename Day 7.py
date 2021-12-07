with open('input.txt') as f:
    numbers = f.readlines()
    numbers = numbers[0].strip("\n").split(",")
    numbers = [i for i in map(int, numbers)]


def calc_fuel_one(seq):
    pos = max(seq,key=seq.count)
    total_fuel = {}
    for pos in range(0, len(seq)):
        track_fuel = 0
        for i in seq:
            fuel = abs(i-pos)
            track_fuel += fuel
        total_fuel[pos] = track_fuel
    return total_fuel

def calc_fuel_two(seq):
    pos = max(seq,key=seq.count)
    total_fuel = {}
    for pos in range(0, len(seq)):
        track_fuel = 0
        for i in seq:
            #fuel = sum(range(1, abs(i-pos)+1))
            n = abs(i-pos)+1
            fuel = int((n*(n+1))/2)
            track_fuel += fuel
        total_fuel[pos] = track_fuel
    return total_fuel

print(min(calc_fuel_one(numbers).values()))
print(min(calc_fuel_two(numbers).values()))
