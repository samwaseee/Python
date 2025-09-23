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

# Find first root
root1 = newton_raphson(2)
print(f"Root 1: {root1:.3f}")

# Deflate: (x - root1) * (ax^2 + bx + c) = x^3 - 6x + 4
a = 1
b = root1
c = (4 - root1**3 + 6*root1) / root1

def f2(x):
    return x**2 + b*x + c

def df2(x):
    return 2*x + b

root2 = newton_raphson(-2, f=f2, df=df2)
root3 = newton_raphson(0.5, f=f2, df=df2)
print(f"Root 2: {root2:.3f}")
print(f"Root 3: {root3:.3f}")