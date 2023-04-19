def stock_list(list_of_art, list_of_cat):
    tab = []
    stri = ''
    for a in list_of_cat:
        asum = 0
        for b in list_of_art:
            if b.startswith(a):
                x = b.split()
                asum += int(x[1])
        tab.append(asum)
    if sum(tab) == 0:
        return ''
    z = 0
    for c in list_of_cat:
        stri += f'({c} : {tab[z]})'
        z += 1
        if len(list_of_cat) == z:
            break
        else:
            stri += ' - '
    return stri