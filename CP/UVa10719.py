def sd(c, k):
    n = len(c) -1
    r = c[0]
    q = []
    q.append(r)
    for i in range(1, n + 1):
        r = r * k + c[i]
        if i < n:
            q.append(r)
    return q, r

while True:
    try:
        k = int(input())
        c = list(map(int, input().strip().split()))
        q,r = sd(c, k)
        print('q(x):', *q)
        print(f"r = {r}")
        print()
    except EOFError:
        break