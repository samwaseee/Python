def f(x):
    return x**3 - 9*x + 1

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

root = bisection(0, 1)
print(f"Root ≈ {root:.3f}")