def convtobin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 10
    rez = ""
    while n > 0:
        rest = n % 2
        rez = str(rest) + rez
        n = n // 2
    return rez


print(convtobin(7))
