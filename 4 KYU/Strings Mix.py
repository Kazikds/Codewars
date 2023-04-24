def mix(s1, s2):
    coun = []
    word = []
    res = []
    alph1 = count(s1)
    alph2 = count(s2)

    for a in range(len(alph1)):
        if alph1[a] < 2 and alph2[a] < 2:
            coun.append(0)
            word.append(0)
        elif alph1[a] > alph2[a]:
            coun.append(alph1[a])
            word.append('1:')
        elif alph2[a] > alph1[a]:
            coun.append(alph2[a])
            word.append('2:')
        elif alph1[a] == alph2[a]:
            coun.append(alph1[a])
            word.append('=:')

    coun = lett(coun)

    coun = zero(coun)
    word = zero(word)
    for a in range(len(coun)):
        res.append(f"{word[a]}{coun[a]}")

    res.sort()
    res.sort(reverse=True, key=len)

    return '/'.join(res)


def zero(list):
    x = list.count(0)
    for a in range(x):
        list.remove(0)
    return list


def count(text):
    from string import ascii_lowercase
    tab = []
    for a in ascii_lowercase:
        tab.append(text.count(a))
    return tab


def lett(lis):
    from string import ascii_lowercase
    tab = []
    for a in range(len(lis)):
        if lis[a] == 0:
            tab.append(0)
        else:
            let = ''
            for b in range(lis[a]):
                let += ascii_lowercase[a]
            tab.append(let)
    return tab