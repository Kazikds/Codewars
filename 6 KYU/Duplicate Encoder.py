def duplicate_encode(word):
    word = word.lower()
    res = ''
    for a in word:
        x = word.count(a.lower())
        if x == 1:
            res += '('
        else:
            res += ')'
    return res