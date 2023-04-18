def title_case(title, minor_words=''):
    sent = ''
    minor = minor_words.lower().split()
    x = -1
    for a in title.split():
        x += 1
        if a.lower() in minor:
            if x == 0:
                sent += a.title() + ' '
            else:
                sent += a.lower() + ' '
        else:
            sent += a.title() + ' '
    return sent.rstrip()