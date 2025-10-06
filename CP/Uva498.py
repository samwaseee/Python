def poly(c,x):
    r = 0
    for coef in c:
        r = r*x + coef
    return r

while True:
    try:
        c = input().strip()
        if not c:
            break
        c = list(map(int, c.split()))
        x = list(map(int, input().strip().split()))

        r = [poly(c, xi) for xi in x]
        print(' '.join(map(str, r)))
    except EOFError:
        break

