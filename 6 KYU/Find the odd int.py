def find_it(seq):
    for a in set(seq):
        x = seq.count(a)
        if x % 2 != 0:
            return a