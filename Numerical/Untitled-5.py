def f(x):
    return x**3 - 6*x + 4
def df(x):
    return 3*x**2 - 6

def newton_raphson(x0, tol=1e-3):
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1

x0 = float(input("Initial guess: "))
root = newton_raphson(x0)
print(f"Root ≈ {root:.3f}")