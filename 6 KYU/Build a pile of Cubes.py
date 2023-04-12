def find_nb(m):
    wyn = 0
    y = 1
    while wyn <= m:
        wyn += y**3
        y += 1
        if wyn == m:
            return y - 1
    return -1