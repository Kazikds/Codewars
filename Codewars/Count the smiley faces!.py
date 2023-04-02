def count_smileys(arr):
    sf = 0
    smfac = [':)', ':D', ':-D', ':~)', ':-)',
             ':~D' ';)', ';D', ';-D', ';~)', ';-)', ';~D']
    for a in arr:
        if a in smfac:
            sf += 1
    return sf