def snail(snail_map):
    x = len(snail_map)
    tab = []
    if snail_map == [[]]:
        return []
    for a in snail_map:
        print(a)
        for b in a:
            tab.append(b)
    snail = []
    for y in range(x):

        for a in range(0 + y, x - y):
            snail.append(tab[a + x * y])
            if len(tab) == len(snail):
                return snail

        for a in range(1 + y, x - y):
            snail.append(tab[(x * (a+1) - 1) - y])
            if len(tab) == len(snail):
                return snail

        for a in range(1 + y, x - y):
            snail.append(tab[x * x - 1 - a - x * y])
            if len(tab) == len(snail):
                return snail

        for a in range(1 + y, x - 1 - y):
            snail.append(tab[(x * x - x + y) - x * a])
            if len(tab) == len(snail):
                return snail

    return snail