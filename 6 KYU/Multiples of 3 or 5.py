def solution(number):
    x = 0
    for a in range(number):
        if a % 3 == 0 or a % 5 == 0:
            x += a
    return x