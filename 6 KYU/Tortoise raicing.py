def race(v1, v2, g):
    tab = []
    if v1 >= v2:
        return None
    x = v2 - v1
    t = g / x
    y = str(t*60).split('.')
    y[1] = '0.' + y[1]
    y[1] = float(y[1])
    tab.append(int(y[0])//60)
    tab.append(int(y[0]) % 60)
    tab.append(int(y[1] * 60))
    return tab