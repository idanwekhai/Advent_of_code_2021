with open('input8.txt') as f:
    patterns = f.readlines()

def make_input(raw):
    cleaned = []
    for line in raw:
        new = line.split()
        seperator = new.index("|")
        new = new[seperator+1:]
        cleaned.append(new)
    return cleaned

def get_digits_one(seq):
    count = 0
    for i in seq:
        lenghts = [(len(j), j) for j in i]
        for k in lenghts:
            if k[0] in [2,3,4,7]:
                count += 1
    return count

##numbers = {0: sorted(set("cagedb")),
##           3: sorted(set("fbcad")),
##           2: sorted(set("gcdfa")),
##           5: sorted(set("cdfbe")),
##           6: sorted(set("cdfgeb")),
##           9: sorted(set("cefabd"))}
##
##def get_digits_two(seq):
##    total = 0
##    for i in seq:
##        num = ""
##        lenghts = [(len(j), j) for j in i]
##        for k in lenghts:
##            if k[0] == 2:
##                num += str(1)
##            elif k[0] == 3:
##                num += str(7)
##            elif k[0] == 4:
##                num += str(4)
##            elif k[0] == 7:
##                num += str(8)
##            else:
##                print(k)
##                num += str(list(numbers.keys())[list(numbers.values()).index(sorted(set(k[1])))])
##        total += int(num)
##    return total
print(numbers)
inputs = make_input(patterns)
print(get_digits_one(inputs))
print(get_digits_two(inputs))
