def f(x):
    return x**3 - 5*x**2 - 29

def secant(x0, x1, tol=1e-3):
    while abs(x1 - x0) > tol:
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x2
    return x1

root = secant(5, 6)
print(f"Root ≈ {root:.3f}")