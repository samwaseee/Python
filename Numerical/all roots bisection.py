def f(x):
    return x**3 - 6*x + 4

def bisection(a, b, tol=1e-3):
    if f(a) * f(b) >= 0:
        print("No root in interval")
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

intervals = [(-4, -1), (0, 1), (1, 3)]
roots = []
for a, b in intervals:
    root = bisection(a, b)
    if root is not None:
        roots.append(round(root, 3))
print("Roots:", roots)