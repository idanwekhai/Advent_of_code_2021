with open('input.txt') as f:
    all_bits = [line.strip() for line in f]
    all_bits_1 = [list(map(int, line)) for line in all_bits]
    all_bits_2 = [seq for seq in zip(*all_bits)]
    
def least_common(lst):
    return min(set(lst), key=lst.count)

def most_common(lst):
    return max(set(lst), key=lst.count)

def get_gamma_epsilon(seq):
    gamma = ""
    epsilon = ""
    for i in seq:
        least_bit = least_common(i)
        most_bit = most_common(i)

        gamma += str(least_bit)
        epsilon += str(most_bit)
        
    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)
    
    return gamma_decimal * epsilon_decimal

def most_or_equal(seq):
    count_1 = seq.count(1)
    count_0 = seq.count(0)

    if count_1 > count_0:
        return 1
    elif count_0 > count_1:
        return 0
    elif count_1 == count_0:
        return 1
        
def less_or_equal(seq):
    count_1 = seq.count(1)
    count_0 = seq.count(0)

    if count_1 < count_0:
        return 1
    elif count_0 < count_1:
        return 0
    elif count_1 == count_0:
        return 0

def keep_most_with_index(index, to_keep, seq):
    
    keep = []
    for i in range(len(seq)):
        if seq[i][index] == to_keep:
            keep.append(seq[i])     
    return keep
                         
def get_oxygen_generator(seq1, index_to_consider = 0):

    in_seq = [seq for seq in zip(*seq1)]
    
    most = most_or_equal(in_seq[index_to_consider])

    new_seq = keep_most_with_index(index_to_consider, most, seq1)

    index_to_consider += 1
    if len(new_seq) == 1:
        return "".join([str(e) for e in new_seq[0]])
    else:
        return get_oxygen_generator(new_seq, index_to_consider=index_to_consider)

def get_co2_scrubber(seq1, index_to_consider = 0):

    in_seq = [seq for seq in zip(*seq1)]
    
    less = less_or_equal(in_seq[index_to_consider])

    new_seq = keep_most_with_index(index_to_consider, less, seq1)

    index_to_consider += 1
    if len(new_seq) == 1:
        return "".join([str(e) for e in new_seq[0]])
    else:
        return get_co2_scrubber(new_seq, index_to_consider=index_to_consider)
    
            
 
oxy = get_oxygen_generator(all_bits_1)
co2 = get_co2_scrubber(all_bits_1)

print(get_gamma_epsilon(all_bits_2))
print(int(oxy, 2) * int(co2, 2))
