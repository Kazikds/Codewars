def diamond(n):
    wor = ''
    tab = []
    if n <= 0 or n % 2 == 0:
        return None
    x = n//2 + 1
    y = 0
    while x != y:
        y += 1
        wor = ' ' * (n//2 - y + 1) + '*' * (y * 2 - 1) + '\n'
        tab.append(wor)
        wor = ''
    y = 1
    for a in range(n):
        if a <= n//2:
            wor += tab[a]
        else:
            a = a - 2 * y
            wor += tab[a]
            y += 1
    return wor