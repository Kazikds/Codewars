def multiplication_table(size):
    tabs = []
    tab = []
    x = 1
    for a in range(1, size + 1):
        tab.append(a)
    tabs.append(tab)
    tab = []
    for a in range(size - 1):
        x += 1
        tab.append(x)
        for b in range(1, size):
            tab.append(x * tabs[0][b])
        tabs.append(tab)
        tab = []
    return tabs