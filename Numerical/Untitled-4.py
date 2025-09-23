def f(x):
    return x**3 - 6*x + 4

intervals = [(-4, -1), (0, 1), (1, 3)]
roots = []
for a, b in intervals:
    root = bisection(a, b)
    if root is not None:
        roots.append(round(root, 3))
print("Roots:", roots)