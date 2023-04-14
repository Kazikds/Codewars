def two_sum(numbers, target):
    tab = []
    y = 1
    z = 0
    for a in numbers:
        x = target - a
        y = 1
        for b in numbers[y:]:
            if len(tab) == 2:
                break
            if (x - b) == 0:
                tab.append(z)
                tab.append(y)
                break
            y += 1
        if len(tab) == 2:
            break
        z += 1
        
    return tab