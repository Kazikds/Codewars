def tower_builder(n_floors):
    tower = []
    flo = []
    for a in range(n_floors * 2 - 1):
        flo.append('*')
    for b in range(0, n_floors):
        tower.insert(0, ''.join(flo))
        flo[b] = ' '
        flo[-(b + 1)] = ' '
    return tower