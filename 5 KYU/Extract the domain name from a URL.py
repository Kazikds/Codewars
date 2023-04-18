def domain_name(url):
    url = url.split('//')
    if len(url) > 1:
        url = url[1]
    else:
        url = url[0]
    url = url.split('ww.')
    if len(url) == 2:
        url = url[1]
    else:
        url = url[0]
    url = url.split('.')
    return url[0]