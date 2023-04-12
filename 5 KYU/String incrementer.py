def increment_string(strng):
    wor1 = ''
    wor2 = ''
    num = '0123456789'
    if len(strng) == 0:
        return '1'
    if strng[-1] in num:
        for a in strng:
            if a not in num and len(wor2) == 0:
                wor1 += a
            elif a not in num and len(wor2) > 0:
                wor1 += wor2 + a
                wor2 = ''
            else:
                wor2 += a
        x = len(wor2)
        print(x)

        wor2 = str((int(wor2)) + 1)
        for b in range(x):
            if len(wor2) != x:
                wor2 = '0' + wor2
            elif len(wor2) == x:
                break
        print(len(wor2))
        if len(wor2) == x:
            return wor1 + wor2
        else:
            return wor1 + wor2[-(x+1):]
    else:
        strng += '1'
        return strng
