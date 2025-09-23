def f(x):
    return x**3 - 6*x +4
def df(x):
    return 3*x**2 - 6

x0 = float(input("Enter the initial guess: "))

def newton_raphson(x0, tol=1e-5):
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1

root = newton_raphson(x0)
print(f"The root is approximately: {root:.3f}")

