def f(x):
    return x**3 - x + 2

def false_position(a, b, tol=1e-3):
    if f(a) * f(b) >= 0:
        print("No root in interval")
        return None
    while abs(b - a) > tol:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

root = false_position(-2, -1)
print(f"Root ≈ {root:.3f}")