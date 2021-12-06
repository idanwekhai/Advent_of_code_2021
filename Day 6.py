from collections import Counter

with open('input.txt') as f:
    
    numbers = f.readlines()
    numbers = numbers[0].strip("\n").split(",")
    numbers = [i for i in map(int, numbers)]


##def model_growth(seq, days):
##    new_seq = seq[:]
##    for i in range(days):
##        for j in range(len(new_seq)):
##            if new_seq[j] != 0:
##                new_seq[j] -= 1
##            elif new_seq[j] == 0:
##                new_seq[j] = 6
##                new_seq.append(8)
##    return len(new_seq)
##
    
def model_growth(seq, days):
    new_seq = Counter(seq)
    print(new_seq)
    for _ in range(days):
        day_0 = new_seq[0]
        for k in range(8):
            new_seq[k] = new_seq[k+1]
        new_seq[6] += day_0
        new_seq[8] = day_0
    return  sum(new_seq.values())
    
print(model_growth(numbers, 80))
print(model_growth(numbers, 256))


