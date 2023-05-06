def digital_root(n):
    n = sek(n)
    print(n)
    if n <= 9:
        return n
    n = sek(n)
    if n <= 9:
        return n
    n = sek(n)
    if n <= 9:
        return n


def sek(y):
    x = 0
    for a in str(y):
        x += int(a)
    return x