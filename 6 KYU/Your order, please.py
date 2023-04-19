def order(sentence):
    x = sentence.split()
    sen = []
    for a in range(1, len(x) + 1):
        for b in x:
            for c in b:
                if c == str(a):
                    sen.append(b)
        if len(sen) == len(x):
            break
    return ' '.join(sen)