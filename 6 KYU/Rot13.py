def rot13(message):
    x = 1
    sente = ''
    tab = []
    for a in 'abcdefghijklmnopqrstuvwxyz':     
        tab.append(a)
    for b in message:
        if b.isalpha():
            x = 1
            for c in tab:
                if b.lower() == c:
                    x += 12
                    break
                x += 1
            if x >= len(tab):
                x -= len(tab)
            if b == b.upper():
                sente += tab[x].upper()
            else:
                sente += tab[x]
        else:
            sente += b
    return sente